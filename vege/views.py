from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse

# Create your views here.
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
    


def delete_recepie(request, id):
    queryset= Recepie.objects.get(id=id)
    queryset.delete()
    return redirect('/recepies/')
    