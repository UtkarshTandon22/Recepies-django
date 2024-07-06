from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='/login/')
def recepies(request):
    if request.method == "POST":
        
        data = request.POST
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')
        

        
        Recepie.objects.create(
            recepie_image = recepie_image,
            recepie_name  = recepie_name,
            recepie_description = recepie_description,
            
            
        )
        
        return redirect('/recepies/')
    queryset = Recepie.objects.all()
    
    if request.GET.get('search'):
        queryset = queryset.filter(recepie_name__icontains = request.GET.get('search'))
    context = {'recepies':queryset}
        
        
        
    return render(request , 'recepies.html',context)

@login_required(login_url='/login/')
def update_recepie(request, id):
    queryset = Recepie.objects.get(id=id)
    
    if request.method == "POST":
        data = request.POST
        
        recepie_image = request.FILES.get('recepie_image')
        recepie_name = data.get('recepie_name')
        recepie_description = data.get('recepie_description')       

        
        queryset.recepie_name = recepie_name
        queryset.recepie_description = recepie_description
        if recepie_image:
            queryset.recepie_image = recepie_image
            
        queryset.save()
        return redirect('/recepies/')    
        
        
    context={'recepie': queryset}
    return render(request , 'update_recepies.html',context)
    

@login_required(login_url='/login/')
def delete_recepie(request, id):
    queryset= Recepie.objects.get(id=id)
    queryset.delete()
    return redirect('/recepies/')


def login_page(request):
    data = {
        'title' : 'Recepies'
    }
    if request.method=="POST":

        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not User.objects.filter(username = username).exists():
            messages.error(request, 'Invalid Username')
            return redirect('/login/')
        
        user = authenticate(username = username , password=password)
        
        if user is None:
            messages.error(request , 'Invalid Password')
            return redirect('login/')
        
        else:
            login(request,user)
            return redirect('/recepies/')
            
            
    return render(request , 'login.html',data)

def logout_page(request):
    logout(request)
    return redirect('/login/')

def register(request):
    if request.method=="POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        
        if user.exists():
            messages.info(request, "Username Already Taken")
            return redirect('/register/')
        
        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        
        messages.info(request, "Account Created Successfully ")
        
        return redirect('/register/')
        
    return render(request , 'register.html')
    