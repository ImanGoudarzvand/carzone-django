from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import mail_admins
from django.contrib import messages

def home(request):
    team_queryset = Team.objects.all()
    featured_cars_queryset = Car.objects.order_by('-created_date').filter(is_featured=True)
    latest_cars_queryset = Car.objects.order_by('-created_date')
    option_values_city_queryset = Car.objects.values_list('city', flat=True).distinct()
    option_values_model_queryset = Car.objects.values_list('model', flat=True).distinct()
    option_values_years_queryset = Car.objects.values_list('year', flat=True).distinct()
    option_values_body_style_queryset = Car.objects.values_list('body_style', flat=True).distinct()

    return render(request, 'pages/home.html', {
        'teams': list(team_queryset),
        'featured_cars': list(featured_cars_queryset),
        'latest_cars': list(latest_cars_queryset),
        'option_values_city_queryset' : list(option_values_city_queryset),
        'option_values_model_queryset': list(option_values_model_queryset),
        'option_values_years_queryset': list(option_values_years_queryset),
        'option_values_body_style_queryset': list(option_values_body_style_queryset)
        })

def about(request):
    queryset = Team.objects.all()
    return render(request, 'pages/about.html', {'teams': list(queryset)})

def services(request):
    return render(request, 'pages/services.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = f'you have a new message from Carzone website regarding {subject}'
        message_body = f'Name: {name} .Email: {email} , phone: {phone} , message: {message} '

        mail_admins(
            email_subject,
            message_body,
            )

        messages.success(request, 'Thank you for contacting us.')
        return redirect('contact')


    return render(request, 'pages/contact.html')
