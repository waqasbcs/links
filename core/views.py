from django.shortcuts import render

# Create your views here.

def home(request):
     return render(request,'core/home.html',{'d':'django'})

def aboutus(request):
    return render(request,'core/aboutus.html')
def contactus(request):
    return render(request,'core/contactus.html')

