from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


# Create your views here.

def index(request):
    if request.method == 'POST':
        project = request.POST['project']
        name = request.POST['name']
        project_id = request.POST['project_id']
        phone = request.POST['phone']
        email = request.POST['email']
        message = request.POST['message']
        user_id = request.POST['user_id']


        contact = Contact(name=name, email=email, project=project, project_id=project_id, phone=phone, message=message, user_id=user_id)
        contact.save()

        # Once it is save then send an email to the user
        # send_mail(
        #     'Inquiry from the Customer' + name ,
        #     'Message is  ' + name + '\n' + email  + message,
        #     'portfoliomshakir@gmail.com',
        #     ['mshakir.munawar123@gmail.com', 'mshakir@stu.jsu.edu'],
        #     fail_silently=False,
        # )


        #  Send email
        send_mail(
            project + ': Inquiry from ' + name ,
            'There has been an inquiry from ' + name  + '\n' + message + '\n\nHere is my Email ID: ' + email + ' and Phone Number: ' + phone,
            'portfoliomshakir@gmail.com',
            ['mshakir.munawar123@gmail.com', 'mshakir@stu.jsu.edu', 'portfoliomshakir@gmail.com'],
            fail_silently=False
        )





        messages.success(request, "Thank you for reaching me out! I will get back with you as soon as possible")
        return redirect('/contacts')
    return render(request, 'contacts/contacts.html')