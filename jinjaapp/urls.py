from django.urls import path
from jinjaapp import views


urlpatterns=[
    path('',views.home,name='my_home'),
    path('contact/',views.home,name='my_contact'),
    path('about/',views.about,name='my_about'),


]