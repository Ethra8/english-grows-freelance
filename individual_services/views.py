from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db.models.functions import Lower

from .forms import IndivServiceForm
from .models import IndivService, IndividualType


def individual_services(request):
    """A view to return the list of individual services with sorting and filtering"""
    
    services = IndivService.objects.all()  # Get all individual services
    all_types = IndividualType.objects.all()  # Get all individual service types

    # Create a dictionary mapping type names to their friendly names
    type_friendly_names = {type.name: type.friendly_name for type in all_types}

    query = None
    selected_types = None
    sort = None
    direction = None

    # Check if any GET parameters were passed for sorting/filtering
    if request.GET:
        # Sorting
        if 'sort' in request.GET:
            sort = request.GET['sort']
            if sort == 'name':
                services = services.order_by('name')
            elif sort == 'price':
                services = services.order_by('price')
            elif sort == 'type':  # Sort by type of service
                services = services.order_by('type__friendly_name')  # Sort by type's friendly name
        
        # Sorting direction
        if 'direction' in request.GET:
            direction = request.GET['direction']
            if direction == 'desc':
                services = services.reverse()  # Reverse the sorted queryset

        # Filter by service type
        if 'type' in request.GET:
            selected_types = request.GET['type'].split(',')
            services = services.filter(type__name__in=selected_types)
        
        # Search functionality
        if 'q' in request.GET:
            query = request.GET['q']
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            services = services.filter(queries)

    current_sorting = f'{sort}_{direction}'  # Track current sorting

    # Map selected types to their friendly names
    selected_type_friendly_names = [type_friendly_names.get(t, t) for t in (selected_types or [])]

     # Join the friendly names into a comma-separated string
    selected_type_friendly_names_str = ' & '.join(selected_type_friendly_names)


    template = 'individual_services/individual_services.html'
    
    context = {
        'services': services,
        'search_term': query,
        'current_types': selected_type_friendly_names_str,  # Clean comma-separated string
        'current_sorting': current_sorting,
        'all_types': type_friendly_names.values(),  # All types with friendly names
        'is_individual_services_view': True,
    }

    return render(request, template, context)


@login_required
def add_service(request):

    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('individual_services'))

    service = None  # Initialize service to None for GET requests
    if request.method == 'POST':
        # Also include request.FILES to allow file upload, in this case
        # the service image.
        form = IndivServiceForm(request.POST, request.FILES)
        if form.is_valid():
            service = form.save()
            messages.success(request, "Service created successfully!")
            return redirect(reverse('pack_details', args=[service.pk]))
        else:
            messages.error(request, "There was an error creating the service.")
    else:
        form = IndivServiceForm()

    template = 'individual_services/add_service.html'
    context = {
        'form': form, 
        'service': service,
    }

    return render(request, template, context )


@login_required
def edit_service(request, service_id):
    """ Edit a product in the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))
    
    service = get_object_or_404(IndivService, pk=service_id)
    
    if request.method == 'POST':
        form = IndivServiceForm(request.POST, request.FILES, instance=service)
        if form.is_valid():
            form.save()
            messages.success(request, 'Service updated successfully!')
            return redirect(reverse('pack_details', args=[service.id]))
        else:
            messages.error(request, 'Failed to update service. Please ensure the form is valid.')
    else:
        form = IndivServiceForm(instance=service)
        messages.info(request, f'You are editing {service.name}')

    template = 'individual_services/edit_service.html'
    context = {
        'form': form,
        'service': service,
    }

    return render(request, template, context)


@login_required
def delete_service(request, service_id):
    """Prompt user to confirm deletion and delete service if confirmed"""
    # Check if the user is an admin or superuser
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, only store owners can do that.')
        return redirect(reverse('home'))

    # Get the service or return a 404 if not found
    service = get_object_or_404(IndivService, pk=service_id)

    # If POST request and confirmation is 'Confirm', delete the service
    if request.method == 'POST' and 'confirm_delete' in request.POST:
        service.delete()
        messages.success(request, f'Service "{service.name}" deleted successfully.')
        return redirect(reverse('individual_services'))

    # If POST request and confirmation is 'Keep', redirect to service details
    elif request.method == 'POST' and 'cancel_delete' in request.POST:
        messages.info(request, f'Service "{service.name}" was not deleted.')
        return redirect(reverse('pack_details', args=[service.id]))

    # Render confirmation page
    template = 'individual_services/delete_confirmation.html'
    context = {
        'service': service,
    }
    return render(request, template, context)


def pack_details(request, service_id):
    """ A view to return the pack details page """
    service = get_object_or_404(IndivService, pk=service_id)

    context = {
        'service': service,
    }

    return render(request, 'individual_services/pack_details.html', context)