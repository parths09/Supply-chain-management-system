from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

# Create your views here.
def login(request):
    if request.method == 'POST':
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']

        # verify if the username password in a given role is valid
        if role=='Customer':
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # return render(request,'customer_home.html',{'username':username})
                return redirect('/customer')
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect("/")

        
        if role=='Manager':
            user = auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                # return render(request,'customer_home.html',{'username':username})
                return redirect('/manager')
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect("/")
        else:
            return redirect('/')
        
    elif request.method == 'GET':
        return render(request,'login.html',{})

def register(request):
    if request.method == 'POST':
        role = request.POST['role']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        cnf_password = request.POST['cnf_password']

        # if role == 'Customer':
        if role == 'Customer' or role == 'Manager':
            if password==cnf_password:

                if User.objects.filter(username=username).exists():
                    messages.info(request,'Username Taken')
                    return redirect('register')
                
                elif User.objects.filter(email=email).exists():
                    
                    messages.info(request,'Email Exists')
                    return redirect('register')
                user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
                user.save()

                print("User created")
                return redirect('/')
            else:   
                messages.info(request,'Password dont match')  
                return redirect('register')
        else:
            return redirect('register')
    else:
        return render(request,'register.html',{})


