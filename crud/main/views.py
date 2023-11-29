from django.shortcuts import render,redirect
from .models import *


def home(request):

    data = Test.objects.all()
 
    
    return render(request, "main/home.html",{"data":data})

def post(request):

    if request.method == "POST":
        data1 = request.POST["ad"]
        data2 = request.POST[ "soyad"]

        data = Test(ad=data1,soyad=data2)
        data.save()
        return redirect("home")


# def delete(request):
    
#     Test.objects.all().delete()


#     return redirect("home")

def update(request):
    if request.method == "POST":

     return redirect("home")
    
def delete(request,id):
   data = Test.objects.get(id=id)

   data.delete()

   return redirect("home")







