from django.db import models

# Create your models here.

class LoginTable(models.Model):
    username= models.CharField(max_length=100,null=True,blank=True)
    password= models.CharField(max_length=50,null=True,blank=True)
    Type= models.CharField(max_length=50,null=True,blank=True)

class ArtistTable(models.Model):
    LOGIN= models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null=True,blank=True)
    address= models.CharField(max_length=500,null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)
    gender= models.CharField(max_length=100,null=True,blank=True)
    contactno= models.BigIntegerField(null=True,blank=True)
    experience= models.CharField(max_length=100,null=True,blank=True)
class ModelTable(models.Model):
    ARTISTID= models.ForeignKey(ArtistTable, on_delete=models.CASCADE)
    modelname= models.CharField(max_length=50,null=True,blank=True)
    type= models.CharField(max_length=100,null=True,blank=True)
    image= models.FileField(null=True,blank=True)
class UserTable(models.Model):
    LOGIN= models.ForeignKey(LoginTable, on_delete=models.CASCADE)
    name= models.CharField(max_length=100,null=True,blank=True)
    address= models.CharField(max_length=500,null=True,blank=True)
    age= models.IntegerField(null=True,blank=True)
    gender= models.CharField(max_length=100,null=True,blank=True)
    contactno= models.BigIntegerField(null=True,blank=True)
    experience= models.CharField(max_length=100,null=True,blank=True)    
class bookingTable(models.Model):
    USER= models.ForeignKey(UserTable, on_delete=models.CASCADE)
    ARTIST= models.ForeignKey(ArtistTable, on_delete=models.CASCADE)
    date= models.DateTimeField(auto_now_add=True,null=True,blank=True)
    status= models.CharField(max_length=100,null=True,blank=True)

class paymentTable(models.Model):
     paymentmethod= models.CharField(max_length=100,null=True,blank=True)
     bookingid=models.ForeignKey(bookingTable,on_delete=models.CASCADE)
     date= models.DateTimeField(null=True,blank=True)

class complaintTable(models.Model):
     USERID= models.ForeignKey(UserTable, on_delete=models.CASCADE)
     complaint= models.CharField(max_length=100,null=True,blank=True)
     reply= models.CharField(max_length=100,null=True,blank=True)
     date= models.DateField(max_length=100,null=True,blank=True)

class feedbackTable(models.Model):
     USERID= models.ForeignKey(UserTable, on_delete=models.CASCADE)
     date= models.DateField(auto_now_add=True)
     feedback= models.CharField(max_length=100,null=True,blank=True)
class notoificationTable(models.Model):
    date= models.DateField(auto_now_add=True)
    notification= models.CharField(max_length=100,null=True,blank=True)



  
    
    
 
    

        
          
              
          

        
                                                                  
    