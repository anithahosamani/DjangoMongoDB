from django.shortcuts import render
from myapp.models import *
from django.http import HttpResponseRedirect
from django.core.mail import EmailMessage
from django.contrib.auth.models import User
from OTAI.settings import oti_url,BASE_DIR
from uuid import uuid4
from django.contrib.auth import authenticate, login, logout

# from mongoengine.django.auth_user import User
# Create your views here.

# Frontend homepage view
def nameOfHomepage(request):
    # render to html page
    return render(request, "frontend-template/index-alt.html", locals())

# Generate random key for activation purpose
def random_key():
    return uuid4().hex

# SignUp page
def nameOfSignUp(request):
    if request.method == "POST":  # post method

        # Get all backend user data
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        website = request.POST.get('website')
        country = request.POST.get('country')
        password = request.POST.get('password')
        # Save Backend database data
        user = User.objects.create(username=email, first_name=name, email=email, password=password)
        user.set_password(password)
        user.save()
        user.is_active= False
        sign_up = UserSignUp.objects.create(user=user, phone=phone, website=website, country=country)

        # Activation key Table save data
        act_usr= ActivateUsers(user=user, is_activated=False, unique_id=random_key())
        act_usr.save()

        # Sending activation link mail
        if email:
            subject="Welcome to OneTochAI"
            act_lnk = '%s/activation/?uqid=%s' %(oti_url, str(act_usr.unique_id))
            message= "Find the link here \n Please click link to activate\n"+act_lnk+"\n Please activate above link"
            email = EmailMessage(subject, message, 'onetouchai@support.org', to=[email])
            email.send()

        return HttpResponseRedirect('/')

    # render to html page
    return render(request, "admin-template/signup.html", locals())

# Activation Views
def nameOfActivation(request):
    xz = request.GET.get('uqid')
    # Activate user unique id valid user or not
    if not ActivateUsers.objects.filter(unique_id=xz, is_activated=True):
        # If valid user
        try:
            abc = ActivateUsers.objects.get(unique_id=xz)
        # If invalid user
        except:
            message = 'Oops!!Invalid token please contact administrator'
            return HttpResponseRedirect('/500/')
        # Updated when user activate link
        abc.is_activated = True
        abc.user.is_active = True
        abc.user.save()
        abc.save()
        email = abc.user.email
        if email:
            subject="Welcome to OneTochAI"
            log_lnk = '%s/login/' %(oti_url)
            message= "User Activated \n Please click link to login\n"+log_lnk+"\n Please Login above link"
            email = EmailMessage(subject, message, 'onetouchai@support.org', to=[email])
            email.send()
    return render(request, 'activate_link.html', locals())


# Login function for activated user can login
def nameOfLogin(request):
    # Get data on browser
    username = request.POST.get('email')
    password = request.POST.get('password')
    # Check authanticate username and password
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            login(request, user)
            # Redirect to a success page.
            return HttpResponseRedirect('/home/')
        else:
            # Return a 'disabled account' error message
            error = "Invalid Username and Password"
    else:
        # Return an 'invalid login' error message.
        error = "Invalid Username and Password"
    return render(request, "admin-template/login.html", locals())


# Contact us function
def nameOfContactUs(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        website = request.POST.get('website')
        contact = Contactus.objects.create(name=name,email=email,message=message,website=website)
        return HttpResponseRedirect('/')
    return render(request, "frontend-template/contact-us.html", locals())


# Pricing Page function/views
def nameOfPricing(request):
    return render(request, "frontend-template/pricing-table.html", locals())


# Admin Homepage For Back end
def nameOfHomePage(request):
    return render(request, "admin-template/index-alt.html", locals())


#Logout function
def nameOfLogout(request):
    logout(request)
    return HttpResponseRedirect('/')
