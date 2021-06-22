from django.shortcuts import render

from vehicles.models import Vehicle, Image

# Create your views here.
def homepage_view(request, *args, **kwargs):

    return render(request, "index.html", {})


def vehicle_sales_view(request, *args, **kwargs):
    vehicle_qs = Vehicle.objects.all()

    vehicle_make = request.GET.get('searchmake')
    vehicle_model = request.GET.get('searchmodel')
    vehicle_year = request.GET.get('searchyear')
    vehicle_exterior = request.GET.get('searchexterior')
    vehicle_interior = request.GET.get('searchinterior')
    vehicle_minprice = request.GET.get('searchminprice')
    vehicle_maxprice = request.GET.get('searchmaxprice')


    if vehicle_make != '' and vehicle_make != 'select make' and vehicle_make is not None:
        vehicle_qs = vehicle_qs.filter(make__icontains=vehicle_make)
    
    if vehicle_model != '' and vehicle_model != 'select model' and vehicle_model is not None:
        vehicle_qs = vehicle_qs.filter(model__icontains=vehicle_model)

    if vehicle_year != '' and vehicle_year != 'select year' and vehicle_year is not None:
        vehicle_qs = vehicle_qs.filter(year__icontains=vehicle_year)

    if vehicle_exterior != '' and vehicle_exterior != 'select exterior color' and vehicle_exterior is not None:
        vehicle_qs = vehicle_qs.filter(exterior_color__icontains=vehicle_exterior)

    if vehicle_interior != '' and vehicle_interior != 'select interior color' and vehicle_interior is not None:
        vehicle_qs = vehicle_qs.filter(interior__icontains=vehicle_interior)

    if vehicle_minprice != '' and vehicle_minprice is not None:
        vehicle_qs = vehicle_qs.filter(listing_price__gte=vehicle_minprice)

    if vehicle_maxprice != '' and vehicle_maxprice is not None:
        vehicle_qs = vehicle_qs.filter(listing_price__lte=vehicle_maxprice)

    context = {
        'all_vehicles': vehicle_qs,
    }

    return render(request, "vehicle_sales.html", context)


def about_view(request, *args, **kwargs):

    return render(request, "about.html", {})

def contact_view(request, *args, **kwargs):

    return render(request, "contact.html", {})

def rentals_view(request, *args, **kwargs):

    return render(request, "rentals.html", {})

def storage_view(request, *args, **kwargs):

    return render(request, "storage.html", {})

def detailing_view(request, *args, **kwargs):

    return render(request, "detailing.html", {})