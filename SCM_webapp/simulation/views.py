from django.shortcuts import render
from django.views.decorators.http import require_POST
from datetime import datetime

# Create your views here.
from django.shortcuts import redirect
from django.contrib import messages
from .simulator import simulate_one_day
from .query import *

def simulation_home(request):
    # date = "2025-04-10"
    date = datetime.now()
    date = datetime.strftime(date,"%Y-%m-%d")
    with open('simulation/date.txt','w') as file:
        file.write(date)
    return render(request,'simulation.html',{'date':date,'seek':0})

@require_POST
def run_simulation(request):
    date = request.POST.get('sim_date')
    seek = request.POST.get('seek')
    
    next_day,seek,logs = simulate_one_day(date,seek) # it will return next along with log maybe
    
    with open('simulation/date.txt','w') as file:
        file.write(next_day[:10])
    messages.success(request, f"Simulation advanced by 1 day! Current day is {next_day}")
    return render(request,'simulation.html',{'date':next_day,'seek':seek,'log_messages':logs})  # display the new day and logs here

def reset_simulation_func(request):
    print('Reseting Simulation...')
    reset_simulation()
    return redirect('/simulation')