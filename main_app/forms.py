from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from phone_field import PhoneFormField

class UserRegisterForm(forms.Form):
    First_Name=forms.CharField(label="First Name",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'25','required':'True','autofocus':'True'}))
    Last_Name=forms.CharField(label="Last Name",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'25','required':'True'}))
    Username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    Phone_Number=forms.CharField(label="Phone Number",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True','pattern':'[0-9]{10}'}))
    Email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    Password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    repeat=forms.CharField(label="Repeat Password",widget=forms.PasswordInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    
class HospitalRegisterForm(UserRegisterForm):
    HospitalName=forms.CharField(label="Hospital Name:",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    Username=forms.CharField(label="Username",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    Phone_Number=forms.CharField(label="Phone Number",widget=forms.TextInput(attrs={'class':'form-control','maxlength':'30','required':'True','pattern':'[0-9]{10}'}))
    Email=forms.EmailField(label="Email",widget=forms.EmailInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    Password=forms.CharField(label="Password",widget=forms.PasswordInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    repeat=forms.CharField(label="Repeat Password",widget=forms.PasswordInput(attrs={'class':'form-control','maxlength':'30','required':'True'}))
    HospitalVerificationDocument=forms.FileField(label="Hospital Verification Document",allow_empty_file=False)
    
