from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth

# Create your views here.
def login(request):
    return render(request,'login.html')



def sighup(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
           if User.objects.filter(username==username):
            print("user taken")
           elif User.objects.filter(email==email):
            print("email taken")
           else:
            user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password1)
            user.save();
            print('user created')
           
        else:
            print("password is not matching..")
        return redirect('/')

    else:
        return render(request,'index.html')