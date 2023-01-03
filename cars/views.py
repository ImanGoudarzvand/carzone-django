from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import Paginator

def cars(request):
    car_queryset = Car.objects.order_by('-created_date')
    paginator = Paginator(car_queryset, 3)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    option_values_city_queryset = Car.objects.values_list('city', flat=True).distinct()
    option_values_model_queryset = Car.objects.values_list('model', flat=True).distinct()
    option_values_years_queryset = Car.objects.values_list('year', flat=True).distinct()
    option_values_body_style_queryset = Car.objects.values_list('body_style', flat=True).distinct()

    return render(request, 'cars/cars.html', {"cars": page_obj,
        'option_values_city_queryset' : list(option_values_city_queryset),
        'option_values_model_queryset': list(option_values_model_queryset),
        'option_values_years_queryset': list(option_values_years_queryset),
        'option_values_body_style_queryset': list(option_values_body_style_queryset)
     })

def car_detail(request, pk):
    single_car = get_object_or_404(Car, pk = pk)
    return render(request, 'cars/car-details.html', {"single_car": single_car})


def search(request):
    searched_car_queryset = Car.objects.order_by('-created_date')
        # searched_car_queryset = searched_car_queryset.filter('')
    
    option_values_city_queryset = Car.objects.values_list('city', flat=True).distinct()
    option_values_model_queryset = Car.objects.values_list('model', flat=True).distinct()
    option_values_years_queryset = Car.objects.values_list('year', flat=True).distinct()
    option_values_body_style_queryset = Car.objects.values_list('body_style', flat=True).distinct()
    option_values_transmission_queryset = Car.objects.values_list('transmission', flat=True).distinct()


    if 'keyword' in request.GET:
        data_match_keyword = request.GET['keyword']
        if data_match_keyword:
            searched_car_queryset = searched_car_queryset.filter(title__icontains=data_match_keyword)

    if 'model' in request.GET:
        data_match_model = request.GET['model']
        if data_match_model:
            searched_car_queryset = searched_car_queryset.filter(model__iexact=data_match_model)

    if 'city' in request.GET:
        data_match_city = request.GET['city']
        if data_match_city:
            searched_car_queryset = searched_car_queryset.filter(city__iexact=data_match_city)

    if 'year' in request.GET:
        data_match_year = request.GET['year']
        if data_match_year:
            searched_car_queryset = searched_car_queryset.filter(year__iexact=data_match_year)

    if 'body_style' in request.GET:
        data_match_body_style = request.GET['body_style']
        if data_match_body_style:
            searched_car_queryset = searched_car_queryset.filter(body_style__iexact=data_match_body_style)

    # if 'min_price' and 'max_price' in request.GET:
    data_match_min_price = request.GET['min_price']
    data_match_max_price = request.GET['max_price']
    if data_match_min_price and data_match_max_price:
        searched_car_queryset = searched_car_queryset.filter(price__gt=data_match_min_price, price__lt=data_match_max_price)


    return render(request, 'cars/search.html', {'searched_cars': list(searched_car_queryset),
    
        'option_values_city_queryset' : list(option_values_city_queryset),
        'option_values_model_queryset': list(option_values_model_queryset),
        'option_values_years_queryset': list(option_values_years_queryset),
        'option_values_body_style_queryset': list(option_values_body_style_queryset),
        'option_values_transmission_queryset': list(option_values_transmission_queryset)


    })