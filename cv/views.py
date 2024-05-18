from django.shortcuts import render,redirect
from .models import MyCv

# Create your views here.
def index(request):
    profile= MyCv.objects.get(id=1)
    context={
        'user':profile,
    }

    return render(request,'cv/profile.html',context)

def about(request):
    profile= MyCv.objects.get(id=1)
    context={
        'user':profile,
    }
    return render(request,'cv/about.html',context)


def contact(request,contact_url):
    if 'git' in contact_url:
        return redirect('https://github.com/Ciiaao')
    elif 'inst' in contact_url:
        return redirect("https://www.instagram.com/soheil___sj?igsh=Yzh4ZXlreW0yNXlw")
    else:
        return redirect('https://www.linkedin.com/in/soheil-javanmardi-a178212b5/')