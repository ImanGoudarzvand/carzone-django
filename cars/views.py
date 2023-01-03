from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator

def cars(request):
    car_queryset = Car.objects.order_by('-created_date')
    paginator = Paginator(car_queryset, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print(page_obj)
    return render(request, 'cars/cars.html', {"cars": page_obj})

def car_detail(request, pk):
    single_car = get_object_or_404(Car, pk = pk)
    return render(request, 'cars/car-details.html', {"single_car": single_car})