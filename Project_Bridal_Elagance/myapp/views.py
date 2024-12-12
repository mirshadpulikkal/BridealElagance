from http.client import HTTPResponse
from django.shortcuts import render
from django.views import View
from.models import*

# Create your views here.

class Login(View):
    def get(self,request): 
        return render (request,'admin/nex.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['passworld']
        login_obj=LoginTable.object.get(username=username,passward=password)
        if login_obj=="admin":
            return HTTPResponse('''<script>alert("done");window.location="/"<script>''')

class Artist(View):
    def get(self,request): 
        return render (request,'admin/artist.html')
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




    
    
    
    
    
    