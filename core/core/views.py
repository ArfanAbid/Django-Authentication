from django.shortcuts import render,redirect
from django.contrib.auth.models import User # importy User 
from django.contrib import messages # for desplaing necessary messages The user
from django.contrib.auth import authenticate,login,logout  # For password matching purposes,for when user are already login and come back later
from django.contrib.auth.decorators import login_required # for necessary permissions like login before use
# Create your views here.

def index(request):
    return render(request, 'index.html')

def Register_user(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name') 
        last_name = request.POST.get('last_name') 
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        # if User.objects.filter(user_name=user_name).exists():
        register_users=User.objects.filter(username=user_name)
        if register_users.exists():
                messages.info(request, "User name already Exists")
                return redirect('/Register')
        
        register_users=User(first_name=first_name,last_name=last_name,username=user_name) 
        register_users.set_password(password)
        register_users.save()
        
        messages.info(request, "Account Created SuccessFully")
        return redirect('/Register')
    
    
    
# OR
    
    # register_users=User.objects.create(user_name=user_name,last_name=last_name,user_name=user_name) 
    # register_users.set_password(password)
    # register_users.save()
    
    return render(request, 'Register.html')









def login_user(request):
    if request.method == 'POST':
        user_name = request.POST.get('user_name')
        password = request.POST.get('password')
        
        if  not User.objects.filter(username=user_name).exists():
            messages.info(request, "Invalid User Name !!!")
            return redirect('/Login')
        
        user=authenticate(username=user_name, password=password)
        
        if user is None:
            messages.info(request, "Invalid Password !!!")
            return redirect('/Login')
        
        else:
            login(request,user)
            return redirect('/Blog')
        

    return render(request, 'login.html')



def logout_page(request):
    logout(request)
    return redirect('/Login')



@login_required(login_url="/login")
def blog(request):
    return render(request, 'Blog.html')