from django.shortcuts import render
from django.views.decorators.http import require_POST

# Create your views here.
from django.shortcuts import redirect
from django.contrib import messages
from .simulator import simulate_one_day

def simulation_home(request):
    date = "2025-04-10"
    return render(request,'simulation.html',{'date':date})

@require_POST
def run_simulation(request):
    date = request.POST.get('sim_date')
    print("Date is :",date)
    next_day = simulate_one_day(date) # it will return next along with log maybe
    messages.success(request, f"Simulation advanced by 1 day! Current day is {next_day}")
    return render(request,'simulation.html',{'date':next_day})  # display the new day and logs here
