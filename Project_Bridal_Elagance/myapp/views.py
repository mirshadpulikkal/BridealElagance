from http.client import HTTPResponse
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from.models import*

# Create your views here.

class Login(View):
    def get(self,request): 
        return render (request,'login.html')
    def post(self,request):
        username=request.POST['username']
        password=request.POST['password']
        login_obj=LoginTable.objects.get(username=username,password=password)
        if login_obj.Type=="admin":
            return HttpResponse('''<script>alert("done");window.location="/adminhome"</script>''')
class adminhome(View):
    def get(self,request): 
        return render (request,'admin/adminhome.html')
class manage_artist(View):
    def get(self,request): 
        artist=ArtistTable.objects.all()
        return render (request,'admin/artist.html',{'obj':artist})
class Payment(View):
    def get(self,request): 
        return render (request,'admin/payment.html')
    
class Booking(View):
    def get(self,request):
        booking=bookingTable.objects.all()  
        return render (request,'admin/viewbooking.html',{'obj':booking})
    
class complaint(View):
    def get(self,request): 
        compaint=complaintTable.objects.all()
        return render (request,'admin/viewcomplaint.html',{'obj':compaint})
class Feedback(View):
    def get(self,request): 
        feedback=feedbackTable.objects.all()
        return render (request,'admin/viewfeedback.html',{'obj':feedback})
class view_models(View):
    def get(self,request): 
        obj=ModelTable.objects.all()
        return render (request,'admin/viewmodels.html',{'obj':obj})
class view_user(View):
    def get(self,request): 
        obj=UserTable.objects.all()
        return render (request,'admin/viewuser.html',{'obj':obj})

class view_notification(View):
    def get(self,request): 
        obj=UserTable.objects.all()
        return render (request,'admin/sendnotification.html')
class send_notification(View):
    def get(self,request): 
        obj=UserTable.objects.all()
        return render (request,'admin/sendnotification.html')
    

    
class Accept_artist(View):
    def get(self,request, ar_id): 
        obj=LoginTable.objects.get(id=ar_id)
        obj.Type="Artist"
        obj.save()
        return HttpResponse('''<script>alert("accepted");window.location="/manage_artist"</script>''')
class Reject_artist(View):
    def get(self,request, ar_id): 
        obj=LoginTable.objects.get(id=ar_id)
        obj.Type="Reject"
        obj.save()
        return HttpResponse('''<script>alert("Rejected");window.location="/manage_artist"</script>''')

    
    
class Accept_user(View):
    def get(self,request, ar_id): 
        obj=LoginTable.objects.get(id=ar_id)
        obj.Type="Artist"
        obj.save()
        return HttpResponse('''<script>alert("accepted");window.location="/manage_artist"</script>''')
class Reject_user(View):
    def get(self,request, ar_id): 
        obj=LoginTable.objects.get(id=ar_id)
        obj.Type="Reject"
        obj.save()
        return HttpResponse('''<script>alert("Rejected");window.location="/manage_artist"</script>''')
