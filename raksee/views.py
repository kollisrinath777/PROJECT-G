from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth



# Create your views here.
def register(request):
    if request.method=='POST':

        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        username=request.POST['username']
        password=request.POST['password']
      

        user=User.objects.create_user(username=username,password=password,first_name=first_name,last_name=last_name)
        user.save();
        print('user_created')
        return redirect('/')
    else:
        return render(request,'register.html')

def contacting(request):
    return render(request,'contact.html')
def aboutvil(request):
    return render(request,"about.html")
def photos(request):
    return render(request,'gallery.html')
def view(request):
    return render(request,'view.html')
