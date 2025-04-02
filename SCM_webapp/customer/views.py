from django.shortcuts import render

# Create your views here.
def customer_home(request):
    if request.method=='POST':
        return render(request,'customer_home.html',{'username': request.user.username})
    else:
        return render(request,'customer_home.html',{'username': request.user.username})