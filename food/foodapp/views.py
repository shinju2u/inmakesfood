from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Chef


# Create your views here.
def demo(request):
    obj= Place.objects.all()
    chef=Chef.objects.all()
    return render(request , "index.html",{'result':obj,'people':chef})
# def contact(request):
#     return render(request , "contact.html")
# def about(request):
#     return render(request , "about.html")
# def detail(request):
#     return HttpResponse("This is our details")
# def thanks(request):
#     return HttpResponse("Thank you for visiting our page")

