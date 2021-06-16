from django.shortcuts import render

from vehicles.models import Vehicle, Image

# Create your views here.
def homepage_view(request, *args, **kwargs):

    return render(request, "index.html", {})


def vehicle_sales_view(request, *args, **kwargs):
    vehicle_qs = Vehicle.objects.all()

    context = {
        'all_vehicles': vehicle_qs,
    }

    return render(request, "vehicle_sales.html", context)