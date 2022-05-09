from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.mail import send_mail, EmailMultiAlternatives
from django.conf import settings
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.template import loader
# Create your views here.

class HomeView(TemplateView):
    template_name = "index.html"

    
class AboutView(TemplateView):
    template_name = "about.html"


class WhatWeDoView(TemplateView):
    template_name = "services.html"


class PortFolioView(TemplateView):
    template_name = "portfolio.html"


class CareerView(TemplateView):
    template_name = "careers.html"


class ContactUsView(TemplateView):
    template_name = "contactus.html"


def ContactUs(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = request.POST.get('subject')

    template = loader.get_template('contact_form.txt')
    context = {
        'name' : name,
        'email' : email,
        'message' : message,
        'subject' : subject,

    }
    message = template.render(context)
    email = EmailMultiAlternatives(
        "You got a Query or Feedback !", message,
        "Company NumDesk"+"- Good News !",
        ["odootest90@gmail.com"]
    )
    email.content_subtype = 'html'
    email.send()
    messages.success(request, 'Message Sent Successfully ! We will contact you as soon as possible ... !')
    return HttpResponseRedirect('/contact-us')
    

def send_mail(request):
    name = request.POST.get('name')
    email = request.POST.get('email')
    message = request.POST.get('message')
    subject = request.POST.get('subject')

    template = loader.get_template('contact_form.txt')
    context = {
        'name' : name,
        'email' : email,
        'message' : message,
        'subject' : subject,

    }
    message = template.render(context)
    email = EmailMultiAlternatives(
        "You got a Resume !", message,
        "Company NumDesk"+"- Good News !",
        ["odootest90@gmail.com"]
    )
    email.content_subtype = 'html'
    file = request.FILES['file']
    email.attach(file.name, file.read(), file.content_type)
    email.send()
    messages.success(request, 'Message Sent Successfully ! We will contact you as soon as possible ...')
    return HttpResponseRedirect('careers')
