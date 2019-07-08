from django.db import models
from phone_field import PhoneField
#from django.contrib.auth.models import AbstractUser
# Create your models here.
#The normal user model can be used for login of all users with only an added field of 
#For Vendors and Hospitals, a new form of login can be created

#--------------------------------------------------------------------------------------------
#Normal User Model : Model For Regular Users
#--------------------------------------------------------------------------------------------
class Normal_User(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    phone_no=PhoneField(verbose_name="Phone Number",null=False,unique=True)     
    
#--------------------------------------------------------------------------------------------
#Vendor Model : Model for Vendors
#--------------------------------------------------------------------------------------------
class Vendor(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    vendor_verification_document=models.FileField(verbose_name="Vendor License",upload_to='license_documents')
    phone_no=PhoneField(verbose_name="Phone Number",null=False,unique=True)
    is_verified=models.BooleanField(default=False)#if is verfied then he can start getting requests
    # from users. Otherwise his account is not activated and although he can add products the user
    #cannot view them.
  
#--------------------------------------------------------------------------------------------
#Medicine Model : Model for information about medicine
#--------------------------------------------------------------------------------------------
class Medicine(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    Medicine_name=models.CharField(verbose_name="Medicine Name",max_length=30,null=False)
    Medicine_price=models.FloatField(verbose_name="Cost Of The Medicine")
    Medicine_dosage=models.IntegerField(verbose_name="Dosage in Milligram(mg)")
    types=(('Schedule 1','Schedule 1'),('Schedule 2','Schedule 2'),('Schedule 3','Schedule 3'),('Schedule 4','Schedule 4'),('Schedule 5','Schedule 5'))
    Medicine_type=models.CharField(verbose_name='Type of Medicine',choices=types,null=False,max_length=50)
    pass

#--------------------------------------------------------------------------------------------
#Hostipitals and clinics Model : Model for hostpital, clinics or medical practitioners
#--------------------------------------------------------------------------------------------

class Hospital(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    hospital_name=models.CharField(verbose_name="Hospital Name",max_length=50)
    
    pass

#--------------------------------------------------------------------------------------------
#Notifications Model : Model for handling notifications i.e: Medicine Order From User To A Vendor
#--------------------------------------------------------------------------------------------
class User_To_Vendor_Order(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    order_details=models.CharField(max_length=100,)
    vendor=models.OneToOneField(Vendor,on_delete=models.SET_NULL,null=True)
    user=models.OneToOneField(Normal_User,on_delete=models.SET_NULL,null=True)
    direction=models.BooleanField(default=True) #whether the notification is from user to vendor or opposite
    #if user sends a request then direction is true else it is false
    high_priority=models.BooleanField(default=False)
    
#--------------------------------------------------------------------------------------------
#Notifications Model : Model for handling notifications i.e: Medicine Order From User To A Vendor
#--------------------------------------------------------------------------------------------

class Hospital_To_Vendor_Order(models.Model):
    timestamp=models.DateTimeField(auto_now_add=True)
    order_details=models.CharField(max_length=100,)
    vendor=models.OneToOneField(Vendor,on_delete=models.SET_NULL,null=True)
    hospital=models.OneToOneField(Hospital,on_delete=models.SET_NULL,null=True)
    direction=models.BooleanField(default=True)#whether the notification is from user to vendor or opposite
    #if hospital sends a request then direction is true else it is false
    high_priority=models.BooleanField(default=True)
    