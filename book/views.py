from django.shortcuts import render
from .models import books,author
def ca(request):
    a=author.objects.all()
    return render(request,'fy.html',{'a':a})

# Create your views here.
