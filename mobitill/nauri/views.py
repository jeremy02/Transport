# Create your views here.
from _threading_local import local
from django.shortcuts import render
from django.http import HttpResponse,Http404
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.template import RequestContext, loader
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404
from django.template.loader import get_template
from django.template import Context
from django.utils import simplejson

from django.shortcuts import redirect, render
from django.core.mail import mail_admins

import json

from django.shortcuts import render
from django.http import HttpResponseBadRequest
from django.core.mail import mail_admins

from django.db.models import Q

#import the forms
from nauri.forms import TerminalForm,UserForm,ClientForm,DeviceForm,Assigned_VehicleForm
# Import the models
from nauri.models import Terminal,User,Client,Device,DeviceUsers,Assigned_Vehicle

"""
def index(request):
    return HttpResponse("Rango says hello world!")
"""
"""def index(request):
    context = RequestContext(request)

    #category_name = decode_url(category_name_url)
    if request.method == 'POST':
        #this is for the registration of the devices on entry
        device_form = TerminalForm(request.POST)

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and ClientForm.
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input
    else:
        device_form = TerminalForm()
        user_form = UserForm()
        client_form = ClientForm()

    context_dict = {'device_form':device_form,'user_form': user_form, 'client_form': client_form}
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('nauri/index.html', context_dict, context)
"""

def index(request):
    context = RequestContext(request)

    #category_name = decode_url(category_name_url)
    if request.method == 'POST':
        #this is for the registration of the devices on entry
        device_form = DeviceForm(request.POST)
        vehicle_form = Assigned_VehicleForm(request.POST)

        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and ClientForm.
        user_form = UserForm(data=request.POST)
        client_form = ClientForm(data=request.POST)

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input
    else:
        device_form = DeviceForm()
        user_form = UserForm()
        client_form = ClientForm()
        vehicle_form = Assigned_VehicleForm(request.POST)

    context_dict = {'device_form':device_form,'user_form': user_form, 'client_form': client_form,'vehicle_form':vehicle_form }
    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('nauri/index.html', context_dict, context)
def device_register(request):
    error=''
    success=''

    # If it's a HTTP POST, we're interested in processing form data.
    if request.POST:
        device_form = DeviceForm(data = request.POST)

        device_name=request.POST['device_name']
        device_serial_code=request.POST['device_serial_code']

        if device_form.is_valid():
            # Save the user's form data to the database.
            device = device_form.save()

            success = 'New Device was successfully created!!'

            # Only executed with jQuery form request
            if request.is_ajax():
                #return HttpResponse('OK')
                #success = 'Device Sucessfully Created.'
                print request.POST
            else:
                # render() a form with data (No AJAX)
                # redirect to results ok, or similar may go here
                pass
        else:
            if device_name == "":
                error = "Please enter the device name"
            elif device_serial_code == "":
                error = "Please enter the device serial code"
            else:
                pass

    context_dict = { 'success':success,'error':error}



    return render(request, 'nauri/form_results.html', context_dict)

def client_register(request):
    registration_error=''
    registration_success=''

    # If it's a HTTP POST, we're interested in processing form data.
    if request.POST:
        # Attempt to grab information from the raw form information.
        # Note that we make use of both UserForm and UserProfileForm.
        user_form = UserForm(data=request.POST)
        profile_form = ClientForm(data=request.POST)

        # If the two forms are valid...
        if user_form.is_valid() and profile_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Now sort out the UserProfile instance.
            # Since we need to set the user attribute ourselves, we set commit=False.
            # This delays saving the model until we're ready to avoid integrity problems.
            profile = profile_form.save(commit=False)
            profile.user = user

            # Did the user provide a profile picture?
            # If so, we need to get it from the input form and put it in the UserProfile model.
            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']

            # Now we save the UserProfile model instance.
            profile.save()
            registration_success = "A new client has been successfully added."

            # Update our variable to tell the template registration was successful.
            #registered = True

        # Invalid form or forms - mistakes or something else?
        # Print problems to the terminal.
        # They'll also be shown to the user.
        else:
            registration_error = "Theres a problem adding a new user.Please try again."

    # Not a HTTP POST, so we render our form using two ModelForm instances.
    # These forms will be blank, ready for user input.
    else:
        user_form = UserForm()
        profile_form = ClientForm()

    context_dict = {'registration_error':registration_error,'registration_success':registration_success}
    return render(request, 'nauri/form_results.html', context_dict)

def search_device(request):
    search_error=''
    search_success=''
    search_warning=''
    details = ''

    # If it's a HTTP GET, we're interested in processing form data.

    if request.GET:
        search_text = request.GET['search-device']
        if search_text is not None and search_text != u"":
            #search_success = "Theres text to search"
            check_device_existence = Device.objects.filter(device_name__icontains=search_text).count()
            #check if the device exists
            if check_device_existence > 0:

                #search_success = "The device exists"
                check_status = Device.objects.filter(device_name__icontains=search_text).exclude(status=True).count()

                if check_status > 0:
                    search_success = "The device exists and can be assigned to a client"
                    details = Device.objects.filter(device_name__icontains=search_text)
                else:
                    search_warning = "The device exists but cannot be assigned to a client"
            else:
                search_error = "The device does not exist"

        else:
            search_error = "Please enter the name of device to be searched"

    else:
        pass



    context_dict = {'search_error':search_error,'search_success':search_success,'search_warning':search_warning,'details':details}


    return render(request, 'nauri/search-results.html', context_dict)

def search_client(request):
    search_client_error=''
    search_client_success=''
    search_client_warning=''
    client_details = ''

    # If it's a HTTP GET, we're interested in processing form data.
    #search_client_error = "The device exists but cannot be assigned to a client"

    if request.GET:
        search_text = request.GET['search-client']
        if search_text is not None and search_text != u"":
            client_details = User.objects.filter(Q(username__icontains=search_text) | Q(client__id_no__icontains=search_text) | Q(first_name__icontains=search_text))
            #check if the user exists
            """if client_details > 0:
                search_client_success = "The device exists and can be assigned to a client"
            else:
                search_client_error = "The device does not exist"
            """
        else:
            search_client_error = "Please enter the name of client."

    else:
        pass




    context_dict = {'search_client_error':search_client_error,'search_client_success':search_client_success,'search_client_warning':search_client_warning,'client_details':client_details}


    return render(request, 'nauri/search-results.html', context_dict)

def client_device_assign(request):
    submit_client_error=''
    submit_client_success=''
    submit_client_warning=''

    # If it's a HTTP POST, we're interested in processing form data.
    #submit_client_error = "The device exists but cannot be assigned to a client"

    # If it's a HTTP POST, we're interested in processing form data.
    if request.POST:
        #submit_client_error = "The device exists but cannot be assigned to a client"
        form = Assigned_VehicleForm(data = request.POST)

        client_id=request.POST['client-id']
        device_id=request.POST['device-id']
        reg_no=request.POST['reg_no']
        sacco_name=request.POST['sacco_name']

        if form.is_valid():
            # Save the user's form data to the database.
            #device = device_form.save()
            #submit_client_success = 'New Device was successfully created!!'

            #find the following instances
            client = Client.objects.get(id=client_id)
            device = Device.objects.get(id=device_id)
            #now assign the device to this client
            device.client = client
            device.status = True
            #save
            device_test = device.save()

            #assign the device to this vehicle after saving the vehicle form
            vehicle_form = form.save()
            #assign device to this vehicle and sacco
            device.assigned_vehicle = vehicle_form
            device_test2 = device.save()
            if not device_test and not device_test2:
                submit_client_success = 'The device was successfully assigned to '+client.user.username
            else:
                submit_client_error = 'The device could not be assigned!Please try again.'

        else:
            if reg_no == "":
                submit_client_error = "Please enter the vehicle registration"
            elif sacco_name == "":
                submit_client_error = "Please enter the sacco name"
            else:
                pass
    else:
        pass


    context_dict = {'submit_client_error':submit_client_error,'submit_client_success':submit_client_success}


    return render(request, 'nauri/form_results.html', context_dict)


def load_device_list(request):
    device_list_error=''
    device_list_success=''
    device_list_warning=''
    device_list_ = ''

    # If it's a HTTP GET, we're interested in processing form data.
    #device_list_success = "The device exists and can be assigned to a client"

    if request.GET:
        check_device_list = Device.objects.filter(status=True).count()
        #check if the device list exists
        if check_device_list > 0:
            device_list = Device.objects.filter(status=True).order_by('assigned_vehicle__date_assigned')
            #device_list_success = "The devices exists to be assigned to users for login details"

            """if check_status > 0:
                search_success = "The device exists and can be assigned to a client"
                details = Device.objects.filter(device_name__icontains=search_text)
            else:
                search_warning = "The device exists but cannot be assigned to a client"
                """
        else:
            device_list_warning = "There are no devices that have been assigned to clients.Please add a device."

    else:
        device_list_error = "Please try again after some few minutes.Sorry."

    context_dict = {'device_list_error':device_list_error,'device_list_success':device_list_success,'device_list_warning':device_list_warning,'device_list':device_list}


    return render(request, 'nauri/search-results.html', context_dict)
