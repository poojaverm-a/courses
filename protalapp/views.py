from django.shortcuts import render
from django.http.response import HttpResponse

# Create your views here.
def home(req):
    return render(req,'home.html',{'name': 'Manisha'})
def contact(req):
    return render(req,'contact.html')
def galary(req):
    return render(req,'galary.html')
def service(req):
    return render(req,'service.html')