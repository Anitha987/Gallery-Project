from django.shortcuts import render
from django.http  import HttpResponse
from .models import Image
import pyperclip


# Create your views here.
def image(request):
    pictures = Image.objects.all()
    return render(request,'image.html',{'gally':pictures})

def search_results(request):

    if 'picture' in request.GET and request.GET["picture"]:
        search_term = request.GET.get("picture")
        searched_pictures = Image.search_by_category(search_term)
        print(searched_pictures)
        message = f"{search_term}"

        return render(request, 'my_gallery/search.html',{"message":message,"pictures": searched_pictures})

    else:
        message = "You haven't searched for any term"
        return render(request, 'my_gallery/search.html',{"message":message})    

def location(request,location):
    image = Location.filter.location(location)
    return render(request,'location.html',{"location":location,'image':image})

   
     

