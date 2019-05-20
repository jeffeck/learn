from django.urls import path
from . import views 

urlpatterns = [
    path('', views.home, name='home'),
    path('instructions/', views.instructions, name='instructions'),
    path('links/', views.links, name='links'),
    
    # path('about/', views.about, name='blog-about'),

]
