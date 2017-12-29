from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    html = "Hello Rango!<br>" \
           "Click <a href='/rango/about/'>here</a> to go to the about page"
    return HttpResponse(html)

def about(request):
    html = "Rango says here is the about page<br>" \
             "Click <a href='/rango/index/'>here</a> to go to the index page"
    return HttpResponse(html)