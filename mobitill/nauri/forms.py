from nauri.models import Terminal,Client,Device,Assigned_Vehicle
from django.contrib.auth.models import User
from django import forms


class TerminalForm(forms.ModelForm):
    device_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'device_name','value':'','placeholder' : 'Device Name e.g(TPS 301)', 'autocomplete' : 'off'}), help_text="Please enter the device name.")
    device_serial_code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'device_serial_code','value':'', 'placeholder' : 'Enter the device serial code', 'autocomplete' : 'off'}),  help_text="Please enter device serial code.")

    class Meta:
        model = Terminal
        fields = ('device_name', 'device_serial_code')
        exclude = ('date_added','status',)

class DeviceForm(forms.ModelForm):
    device_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'device_name','value':'','placeholder' : 'Device Name e.g(TPS 301)', 'autocomplete' : 'off'}), help_text="Please enter the device name.")
    device_serial_code = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'device_serial_code','value':'', 'placeholder' : 'Enter the device serial code', 'autocomplete' : 'off'}),  help_text="Please enter device serial code.")

    class Meta:
        model = Device
        fields = ('device_name', 'device_serial_code')
        exclude = ('date_added','status','client',)


class UserForm(forms.ModelForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'firstname','value':'','placeholder' : "Enter client's first name", 'autocomplete' : 'off'}), help_text="Please enter firstname.")
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'lastname','value':'', 'placeholder' : "Enter client's last name", 'autocomplete' : 'off'}),  help_text="Please enter lastname.")
    username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'username','value':'','placeholder' : "Enter preffered username", 'autocomplete' : 'off'}), help_text="Please enter a username.")
    email = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'email','value':'','placeholder' : "Enter client's email address.", 'autocomplete' : 'off'}),  help_text="Please enter an email address.")
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control' ,'id':'password','value':'','placeholder' : "Enter client's password", 'autocomplete' : 'off'}), help_text="Please enter a password.")

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email', 'password']

class Assigned_VehicleForm(forms.ModelForm):
    reg_no = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'reg_no','value':'','placeholder' : "Vehicle registration number", 'autocomplete' : 'off'}), help_text="Please enter vehicle registration no.")
    sacco_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'sacco_name','value':'', 'placeholder' : "Enter the sacco name", 'autocomplete' : 'off'}),  help_text="Please enter sacco name.")

    class Meta:
        model = Assigned_Vehicle
        fields = ['reg_no','sacco_name']

class ClientForm(forms.ModelForm):
    phone= forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'phone','value':'','placeholder' : "Enter client's phone number", 'autocomplete' : 'off'}), help_text="Please enter phone number.")
    id_no = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'id_no','value':'', 'placeholder' : 'Enter ID No/Passport No.', 'autocomplete' : 'off'}),  help_text="Please enter an idno.")
    address = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'address','value':'', 'placeholder' : "Enter client's address.", 'autocomplete' : 'off'}),  help_text="Please enter the address.")
    zipcode = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'zipcode','value':'', 'placeholder' : 'Enter the zip code.', 'autocomplete' : 'off'}),  help_text="Enter the zipcode.")
    city = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'city','value':'','placeholder' : 'Enter the city/town of residence', 'autocomplete' : 'off'}), help_text="Please enter the city.")
    bank_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'bank_name','value':'','placeholder' : "Enter client's bank name", 'autocomplete' : 'off'}), help_text="Please enter bank name.")
    account_no = forms.IntegerField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'account_no','value':'', 'placeholder' : 'Enter the client\s bank account number.', 'autocomplete' : 'off'}),  help_text="Please enter account number.")
    kra_pin = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'kra_pin','value':'', 'placeholder' : "Enter the client's KRA PIN.", 'autocomplete' : 'off'}),  help_text="Please enter the KRA PIN.")

    class Meta:
        model = Client
        fields = ('phone','id_no','address','zipcode','city','bank_name','account_no','kra_pin')
        exclude = ('date_added',)

"""
class LoginForm(forms.Form):
    login_username = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control' ,'id':'login_username','value':'','placeholder' : 'Enter your username', 'autocomplete' : 'off'}), help_text="Please enter phone number.")
    login_password = forms.IntegerField(widget=forms.PasswordInput(attrs={'class' : 'form-control' ,'id':'login_password','value':'', 'placeholder' : 'Enter your password.', 'autocomplete' : 'off'}),  help_text="Enter your password")

    class Meta:
        fields = ['login_username','login_password']
"""