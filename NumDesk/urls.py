from django.urls import path
from .views import *


app_name = "NumDesk"

urlpatterns = [
    path("", HomeView.as_view(), name="home"),
    path("about/", AboutView.as_view(), name="about"),
    path("services/", WhatWeDoView.as_view(), name="services"),
    path("portfolio/", PortFolioView.as_view(), name="portfolio"),
    path("careers/", CareerView.as_view(), name="careers"),
    path("contact-us/", ContactUsView.as_view(), name="contact-us"),
    path("contactus", ContactUs, name="contactus"),
    path("send_mail", send_mail, name="send_mail"),
]