from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username= models.CharField(max_length=100,null=True,blank=True)
    password= models.CharField(max_length=50,null=True,blank=True)
    Type= models.CharField(max_length=50,null=True,blank=True)

class ArtistTable(models.Model):
    name= models.CharField(max_length=100,null=True,blank=True)
    address= models.CharField(max_length=500,null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)
    gender= models.CharField(max_length=100,null=True,blank=True)
    contactno= models.BigIntegerField(null=True,blank=True)
    experience= models.CharField(max_length=100,null=True,blank=True)
class ModelTable(models.Model):
    ARTISTID= models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    modelname= models.CharField(max_length=50,null=True,blank=True)
    type= models.CharField(max_length=100,null=True,blank=True) 
    image= models.ImageField(null=True,blank=True,upload_to='arimage')
class UserTable(models.Model):
    LOGIN= models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null=True,blank=True)
    address= models.CharField(max_length=500,null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)
    gender= models.CharField(max_length=100,null=True,blank=True)
    contactno= models.BigIntegerField(null=True,blank=True)
    experience= models.CharField(max_length=100,null=True,blank=True)    
class bookingTable(models.Model):
    USERID= models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    date= models.DateTimeField(null=True,blank=True)
    replay= models.CharField(max_length=100,null=True,blank=True)
class paymentTable(models.Model):
     paymentmethod= models.CharField(max_length=100,null=True,blank=True)
     bookingid= models.CharField(max_length=50,null=True,blank=True)
     date= models.CharField(max_length=100,null=True,blank=True)
     time= models.CharField(max_length=100,null=True,blank=True)
class complaintTable(models.Model):
     complaint= models.CharField(max_length=100,null=True,blank=True)
class feedbackTable(models.Model):
     feedback= models.CharField(max_length=100,null=True,blank=True)
class notoificationTable(models.Model):
    notification= models.CharField(max_length=100,null=True,blank=True)



  
    
    
 
    

        
          
              
          

        
                                                                  
    