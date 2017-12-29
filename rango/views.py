from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    context_dict = {'boldmessage': "Crunchy, creamy, cookie, candy, cupcake"}
    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    html = "Rango says here is the about page<br>" \
             "Click <a href='/rango/index/'>here</a> to go to the index page"
    return HttpResponse(html)