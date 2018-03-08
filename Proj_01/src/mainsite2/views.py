from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from .models import Post
from django.shortcuts import HttpResponse

# Create your views here.
def homepage(request):
    template =get_template('index.html')
    posts    =Post.objects.all()
    now      =datetime.now()
    html     =template.render(locals())
    return HttpResponse(html)
    
def showpost(request, slug):
    template =get_template('post.html')
    try:
        post= Post.objects.get(slug=slug)
        if post != None:
            html= template.render(locals())
            return HttpResponse(html)
    except:
            return HttpResponse('/')

def homepage2(request):
    template =get_template('index2.html')
    posts    =Post.objects.all()
    now      =datetime.now()
    html     =template.render(locals())
    return HttpResponse(html)

def showpost2(request, slug):
    template =get_template('post2.html')
    try:
        post2= Post.objects.get(slug=slug)
        if post2 != None:
            html= template.render(locals())
            return HttpResponse(html)
    except:
            return HttpResponse('/index2')

def about(request):
    template=get_template('my_self.html')
    html=template.render(locals())
    return HttpResponse(html)
