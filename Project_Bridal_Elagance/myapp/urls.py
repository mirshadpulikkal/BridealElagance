from django.urls import path

from .views import *

urlpatterns = [
    path('',Login.as_view(), name='login'),
     path('adminhome',adminhome.as_view(),name='adminhome'),
    path('artist',Artist.as_view(),name='artist'),
    path('payment',Payment.as_view(),name='payment'),
    path('booking',Booking.as_view(),name='booking'),
    path('complaint',complaint.as_view(),name='complaint'),
    path('feedback',Feedback.as_view(),name='feedback'),
    path('models',Models.as_view(),name='models'),
    path('user',user.as_view(),name='user'),  

]