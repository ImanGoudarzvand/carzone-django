from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages
from django.core.mail import mail_admins

# Create your views here.
def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        user_id = request.POST['user_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if Contact.objects.filter(user_id = user_id, car_id = car_id).exists():
            messages.error(request, 'Your already has been submitted a request.')
 
        else:

            contact = Contact(car_id = car_id, car_title = car_title, user_id = user_id, first_name = first_name,
            last_name = last_name, customer_need = customer_need, city = city, state = state, email = email, 
            phone = phone, message = message)

            mail_admins(
                'New Car Inquiry',
                f'You have a new car inquiry for the car {car_title}, please log in to your admin panel for more info ',
                
            )

            contact.save()
            messages.success(request, 'Your request has been submitted, we will get to you shortly.')
        return redirect('/cars/'+ car_id)


        


        



