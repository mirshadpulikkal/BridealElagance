from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from.models import*

# Create your views here.

class Login(View):
    def get(self,request): 
        return render (request,'admin/login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username,password=password)
        if login_obj.Type=="admin":
            return HttpResponse('''<script>alert("done");window.location="/adminhome"</script>''')
class adminhome(View):
    def get(self,request): 
        return render (request,'admin/adminhome.html')
class Artist(View):
    def get(self,request): 
        artist=ArtistTable.objects.all()
        return render (request,'admin/artist.html',{'a':artist})
class Payment(View):
    def get(self,request): 
        return render (request,'admin/payment.html')
class Booking(View):
    def get(self,request): 
        return render (request,'admin/viewbooking.html')
class complaint(View):
    def get(self,request): 
        return render (request,'admin/viewcomplaint.html')
class Feedback(View):
    def get(self,request): 
        return render (request,'admin/viewfeedback.html')
class Models(View):
    def get(self,request): 
        obj=ModelTable.objects.all()
        return render (request,'admin/viewmodels.html',{'obj':obj})
class user(View):
    def get(self,request): 
        obj=UserTable.objects.all()
        return render (request,'admin/viewuser.html')




    
    
    
    
    
    