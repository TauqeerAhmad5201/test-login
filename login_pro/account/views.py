from this import d
from django.shortcuts import render, redirect
from django.http import HttpResponse, request 
from django.contrib.auth.models import User
from django.contrib import messages
from account.models import Signupdata
from django.contrib import redirects
from django.contrib.auth import authenticate, login,logout


# Create your views here.
def index(request):
    return render(request,'index.html')

def join(request):
    return render(request,'join.html')

def signup(request):
    return render(request,'signup.html')

def signupsent(request):
    if request.method == 'POST':
        firstname = request.POST['fname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
    
        if password==password2:
            if Signupdata.objects.filter(email=email).exists():
                messages.info(request, 'Email already registered.')
                return redirect('/signup')
            
            elif Signupdata.objects.filter(username=username).exists():
                messages.info(request, 'Username already registered.')
                return redirect('/signup')
            else:
                ins = Signupdata(firstname=firstname, lastname=lastname,email=email, password=password, password2=password2,username=username)
                ins.save()

                # myuser = User.objects.create_user(username = username,firstname=firstname, lastname=lastname,email=email, password1=password1, password2=password2)
        # myuser.first_name = firstname
        # myuser.last_name = lastname 
                # myuser.save()
                messages.success(request, "Welcome ! Your Account Created !")
                return redirect('/account')
        
        else:
            print('Passwords not matching.')

    else:
        return HttpResponse('404- USE POST')

def loginsent(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password') 
        print(username,password)
        user = authenticate(username=username, password = password)
        print(user)
        if user is not None:
            login(request,user)
            messages.success(request,'Successfully Logged In as {email}')
        else:
            messages.error(request,'Sorry ! Invalid Credentials')
            # return HttpResponse('login failed')
            return redirect('/account')
    else:
        return HttpResponse('HAVE POST !')