from django.urls import path
from . import views  # This imports blog/views.py

urlpatterns = [
    path('', views.home, name='home'),  # This line expects an 'index' view in blog/views.py
    path('specific',views.specific,name='specific'),

    path('getResponse',views.getResponse,name='getResponse')
   
]
