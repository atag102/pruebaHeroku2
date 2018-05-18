from django.urls import path
from APH1.views import home

urlpatterns = [
    path('', home,name='home'),
]