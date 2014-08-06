from django.db import models

# Create your models here.

from django.db import models
import datetime
from django.utils import timezone
from django.utils.http import urlquote
from django.utils.translation import ugettext_lazy as _
from django.core.mail import send_mail
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db.models import IntegerField, Model
from django.core.validators import MaxValueValidator, MinValueValidator

from django.contrib.auth.models import User

class Terminal(models.Model):
    device_name = models.CharField(max_length=128, blank=False)
    device_serial_code = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return u"%s %s" %(self.device_name,self.device_serial_code)

class Client(models.Model):
    #This line is required.Links user profile to a user model instance
    user = models.OneToOneField(User)

    #The additional attributes we wish to include
    id_no = models.IntegerField(max_length=128)
    phone = models.IntegerField(max_length=128)
    address = models.CharField(max_length=128)
    zipcode = models.IntegerField(max_length=128)
    city = models.CharField(max_length=128)
    bank_name = models.CharField(max_length=128)
    account_no = models.IntegerField(max_length=128)
    kra_pin = models.IntegerField(max_length=128)
    date_added = models.DateTimeField(auto_now=True)

class Assigned_Vehicle(models.Model):
    reg_no = models.CharField(max_length=128, blank=False)
    sacco_name = models.CharField(max_length=128)
    date_assigned = models.DateTimeField(auto_now=True)
    
class Device(models.Model):
    client = models.ForeignKey(Client,null=True, blank=True, default = None)
    assigned_vehicle = models.ForeignKey(Assigned_Vehicle,null=True, blank=True, default = None)
    device_name = models.CharField(max_length=128, blank=False)
    device_serial_code = models.CharField(max_length=128)
    date_added = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return u"%s %s" %(self.device_name,self.device_serial_code)



class DeviceUsers(models.Model):
    #This line is required.Links Client and Device to a DeviceUsers model instance
    client = models.ForeignKey(Client)
    device = models.ForeignKey(Device)
    #The additional attributes we wish to include
    firstname = models.CharField(max_length=128)
    lastname = models.CharField(max_length=128)
    email = models.CharField(max_length=128)
    username = models.CharField(max_length=128)
    password = models.CharField(max_length=128)





