from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

from django.contrib.auth.models import Group

roles = ['Customer', 'Manager', 'Supplier']
for role in roles:
    Group.objects.get_or_create(name=role)

def verify_user(username, password, group_name):
    
    user = auth.authenticate(username=username, password=password)
    if user and user.groups.filter(name=group_name).exists():
        return user
    return None

def login(request):
    if request.method == 'POST':
        role = request.POST['role']
        username = request.POST['username']
        password = request.POST['password']

        # verify if the username password in a given role is valid
        if role in roles:
            user = verify_user(username, password, role)

            if user is not None:
                auth.login(request,user)
                return redirect(f'/{role.lower()}')
            
            else:
                messages.info(request,'Invalid Credentials!')
                return redirect("/")
        
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

        if password!=cnf_password:
            messages.info(request,'''Password don't match''')  
            return redirect('register')
        
        if User.objects.filter(username=username).exists():
            messages.info(request, 'Username Taken')
            return redirect('register')
        
        if User.objects.filter(email=email).exists():
            messages.info(request, 'Email Exists')
            return redirect('register') 
        group= Group.objects.get(name=role)
        

        user = User.objects.create_user(first_name=first_name,last_name=last_name,username=username,password=password,email=email)
        group.user_set.add(user)
        user.save()

        print(f"{role} created")
        return redirect('/')
    
    else:
        return render(request,'register.html',{})
    
def logout(request):
    auth.logout(request)
    request.session.flush()  # Clears session data
    return redirect('/')     # Redirect to login