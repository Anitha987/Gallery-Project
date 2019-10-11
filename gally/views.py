from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image


# Create your views here.
def image(request):
    pictures = Image.objects.all()
    return render(request,'image.html',{'gally':pictures})

   
