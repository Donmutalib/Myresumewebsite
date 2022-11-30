from django.urls import path
from . import views

app_name = 'backendkola_app'

urlpatterns = [
    path('', views.index, name = 'index')
]
