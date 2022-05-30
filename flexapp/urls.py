from django.contrib import admin
from django.urls import path
from flexapp import views

urlpatterns = [
    path('',views.home, name="home"),
    path('detail',views.detail, name="detail"),
    path('feed',views.feed, name="feed"),
    path('product',views.product, name="product"),
    path('registration',views.registration, name="registration"),
]