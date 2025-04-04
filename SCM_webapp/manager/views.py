from django.shortcuts import render

# Create your views here.

def manager_home(request):
    if request.method=='POST':
        return render(request,'manager_home.html',{'username': request.user.username})
    else:
        return render(request,'manager_home.html',{'username': request.user.username})
    

def manager_shipments(request):
    pass