from django.urls import path

from .views import *

urlpatterns = [
    path('',Login.as_view(), name='login'),
     path('adminhome',adminhome.as_view(),name='adminhome'),
    path('manage_artist',manage_artist.as_view(),name='manage_artist'),
    path('view_payment',Payment.as_view(),name='payment'),
    path('view_booking',Booking.as_view(),name='booking'),
    path('view_complaint',complaint.as_view(),name='complaint'),
    path('view_feedback',Feedback.as_view(),name='feedback'),
    path('view_models',view_models.as_view(),name='models'),
    path('view_user',view_user.as_view(),name='view_user'),  
    path('view_notification',view_notification.as_view(),name='view_notification'),
    path('send_notification',send_notification.as_view(),name='send_notification'),
    path('Accept_artist/<int:ar_id>',Accept_artist.as_view(),name='Accept_artist'),
    path('Reject_artist/<int:ar_id>',Reject_artist.as_view(),name='Reject_artist'),
    path('Accept_user/<int:ar_id>',Accept_artist.as_view(),name='Accept_user'),
    path('Reject_user/<int:ar_id>',Reject_artist.as_view(),name='Reject_user'),
]
