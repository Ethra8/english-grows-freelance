
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.shortcuts import HttpResponse
from django.views.decorators.http import require_POST
from django.contrib import messages
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout


from bag.contexts import bag_contents
from individual_services.models import IndivService
from profiles.models import UserProfile

from .forms import OrderForm
from .models import Order, OrderLineItem

import stripe
import json


@require_POST
def cache_checkout_data(request):
    try:
        pid = request.POST.get('client_secret').split('_secret')[0]
        stripe.api_key = settings.STRIPE_SECRET_KEY
        stripe.PaymentIntent.modify(pid, metadata={
            'bag': json.dumps(request.session.get('bag', {})),
            'username': request.user,
        })
        return HttpResponse(status=200)
    except Exception as e:
        messages.error(request, 'Sorry, your payment cannot be \
            processed right now. Please try again later.')
        return HttpResponse(content=e, status=400)


def checkout(request):
    if not request.user.is_authenticated:
        # If the user is not authenticated,
        # show an error message and redirect to login page.
        messages.error(request, "For your own security \
        and data protection, please login or create an \
        account to proceed to checkout.")
        return redirect('account_login')  # noqa: redirect to login page

    stripe_public_key = settings.STRIPE_PUBLIC_KEY
    stripe_secret_key = settings.STRIPE_SECRET_KEY

    if request.method == 'POST':
        bag = request.session.get('bag', {})

        form_data = {
            'full_name': request.POST['full_name'],
            'email': request.POST['email'],
        }

        order_form = OrderForm(form_data)
        if order_form.is_valid():
            # Create the order but don't commit yet
            order = order_form.save(commit=False)

            # Add the authenticated user profile to the order if
            # the user is authenticated
            if request.user.is_authenticated:
                profile = UserProfile.objects.get(user=request.user)
                order.user_profile = profile

            # Add Stripe Payment ID and the original bag (JSON serialized)
            pid = request.POST.get('client_secret').split('_secret')[0]
            order.stripe_pid = pid
            order.original_bag = json.dumps(bag)
            order.save()

            # Add line items to the order
            for item_id, item_data in bag.items():
                try:
                    service = IndivService.objects.get(id=item_id)
                    if isinstance(item_data, int):
                        # Create the OrderLineItem
                        order_line_item = OrderLineItem(
                            order=order,
                            service=service,
                            quantity=item_data,
                        )
                        order_line_item.save()
                except IndivService.DoesNotExist:
                    messages.error(request, (
                        "One of the services in your bag wasn't found in our \
                        database. "
                        "Please call us for assistance!")
                    )
                    order.delete()  # Delete the incomplete order
                    return redirect(reverse('view_bag'))

            # After adding all line items, update the order totals
            order.update_total()

            # Change the order status to 'processing' and save the order again
            order.status = 'processing'
            order.save()

            # Send the confirmation email
            order.send_confirmation_email()

            # Clear the session bag after the order is successfully processed
            request.session['bag'] = {}

            # Redirect to checkout success page
            return redirect(reverse('checkout_success',
                            args=[order.order_number]))
        else:
            print(order_form.errors)
            messages.error(request, 'There was an error \
            with your form. Please double-check your information.')

        # If form is invalid, render the checkout page again
        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
        }
        return render(request, template, context)

    else:  # Handle GET request
        bag = request.session.get('bag', {})
        if not bag:
            messages.error(request, "There's nothing in \
            your bag at the moment")
            return redirect(reverse('individual_services'))

        current_bag = bag_contents(request)
        total = current_bag['grand_total']
        stripe_total = round(total * 100)
        stripe.api_key = stripe_secret_key
        intent = stripe.PaymentIntent.create(
            amount=stripe_total,
            currency=settings.STRIPE_CURRENCY,
        )

        order_form = OrderForm()

        if not stripe_public_key:
            messages.warning(request, 'Stripe public key is missing. \
            Did you forget to set it in your environment?')

        template = 'checkout/checkout.html'
        context = {
            'order_form': order_form,
            'stripe_public_key': stripe_public_key,
            'client_secret': intent.client_secret,
        }

        return render(request, template, context)


@login_required
def checkout_success(request, order_number):
    """
    Handle successful checkouts.
    Only the authenticated user who placed the order can view it.
    """
    # Fetch the order based on the order_number from the URL
    order = get_object_or_404(Order, order_number=order_number)

    # Ensure the order has an associated user_profile and the user is the owner
    if not order.user_profile or order.user_profile.user != request.user:
        # If the user is not the owner, show an error message and redirect
        messages.error(request, "You do not have permission to \
        view this order.")
        logout(request)  # Logs out the current user
        return redirect('home')  # Redirect to the home page

    # Process the order
    save_info = request.session.get('save_info')
    grand_total = order.grand_total

    # Save the order (if necessary)
    order.save()

    # Show success message
    messages.success(request, f'Order successfully processed! \
        Your order number is {order_number}. A confirmation \
        email will be sent to {order.email}.')

    # Clear the shopping bag from the session
    if 'bag' in request.session:
        del request.session['bag']

    # Render the success page
    template = 'checkout/checkout_success.html'
    context = {
        'order': order,
    }

    return render(request, template, context)
