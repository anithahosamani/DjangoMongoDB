"""OTAI URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from myapp.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url('^$', nameOfHomepage, name="homepage"),  # HomePage front end url
    url('^contact-us', nameOfContactUs, name="contact_us"), # Contact Us url
    url('^pricing', nameOfPricing, name="pricing"), # Pricing url
    url('^sign-up/$', nameOfSignUp, name="sign-up"),  # SignUpPage url
    url(r'^activation/$', nameOfActivation, name='activation'),  # Activation url
    url('^login/$', nameOfLogin, name="login"),  # Login url
    url('^home', nameOfHomePage, name="home"),  # Admin Home page backend
    url('^logout', nameOfLogout, name="logout"), #Logout

]
