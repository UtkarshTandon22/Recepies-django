from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse

def home(request):
    
    peoples = [
        {'name' : 'Utkarsh' , 'age' :20},
        {'name' : 'Vijay' , 'age' :17},
        {'name' : 'Mayank' , 'age' :23},
        {'name' : 'Himanshu' , 'age' :25},
        {'name' : 'Krati' , 'age' :63},
    ]
    
    for people in peoples:
        if people['age'] :
            print("Yes")
    
    vegetables = ['Pumpkin' , 'Carrot' , 'Cucumber']
    
    for people in peoples:
        print(people)
    
    return render(request , "home/index.html", context = {'page' : 'Django 2023 tutorial','peoples' : peoples , 'vegetables': vegetables})

def about(request):
    context = {'page' : "About"}
    
    return render(request , "home/about.html" , context)


def contact(request):
    context = {'page' : "Contact"}
        
    return render(request , "home/contact.html" , context)
    
    
                        

def success_page(request):
    print("*" * 10)
    return HttpResponse("<h1>Hey this is a success page</h1>")