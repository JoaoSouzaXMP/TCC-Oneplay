from django.urls import path
from .views import index, info

urlpatterns = [
    path('', index, name='index'),
    path('info', info, name='info'),
]