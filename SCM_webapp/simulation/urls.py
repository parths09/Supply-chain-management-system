from django.urls import path
from . import views

urlpatterns = [
    path('', views.simulation_home , name='simulation home'),
    path('run-simulation', views.run_simulation, name='run_simulation'),
]