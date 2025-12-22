from django.shortcuts import render, redirect, reverse, HttpResponse
from django.shortcuts import get_object_or_404
from django.contrib import messages

from individual_services.models import IndivService


def view_bag(request):
    """ A view that renders the bag contents page """
    return render(request, 'bag/bag.html')


def add_to_bag(request, item_id):
    """ Add a quantity of the specified product to the\
    shopping bag """
    try:
        service = get_object_or_404(IndivService, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        redirect_url = request.POST.get('redirect_url')
        bag = request.session.get('bag', {})

        if item_id in list(bag.keys()):
            bag[item_id] += quantity
            messages.success(request, f'Updated {service.name}\
            to {bag[item_id]}')
        else:
            bag[item_id] = quantity
            messages.success(request, f'Added {service.name}\
            to your bag')

        request.session['bag'] = bag

        return redirect(redirect_url)

    except Exception as e:
        messages.error(request, f'Error adding\
        item to bag: {e}')
        return HttpResponse(status=500)


def adjust_bag(request, item_id):
    """Adjust the quantity of the specified product to the\
    specified amount"""
    print(f"Adjusting item: {item_id}")  # Debug statement
    try:
        service = get_object_or_404(IndivService, pk=item_id)
        quantity = int(request.POST.get('quantity'))
        bag = request.session.get('bag', {})

        if quantity >= 1:
            bag[item_id] = quantity
            messages.success(request, f'Quantity of\
            {service.name} successfully updated')
        else:
            messages.error(request, f'Failed to update\
            {service.name}')

        request.session['bag'] = bag
        return redirect(reverse('bag'))

    except Exception as e:
        messages.error(request, f'Error updating\
        item: {e}')
        return HttpResponse(status=500)


def remove_bag_item(request, item_id):
    """Remove the item from the shopping bag and redirect 
    to the bag page.
    """
    try:
        # Get the service to display in messages
        service = get_object_or_404(IndivService, pk=item_id)

        # Access the shopping bag session
        bag = request.session.get('bag', {})

        # Remove the item if it exists
        if str(item_id) in bag:
            bag.pop(str(item_id))
            messages.success(request, f'Successfully removed\
            "{service.name}" from your bag.')
        else:
            messages.warning(request, f'Item "{service.name}"\
            was not found in your bag.')

        # Update the session bag
        request.session['bag'] = bag

        # Redirect to the shopping bag template
        return redirect(reverse('bag'))

    except Exception as e:
        # Handle unexpected errors and show an error message
        messages.error(request, f'Error removing item: {e}')
        return redirect(reverse('bag'))
