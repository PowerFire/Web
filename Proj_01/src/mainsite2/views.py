from django.shortcuts import render
from django.template.loader import get_template
from datetime import datetime
from .models import Post, Product
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
    html     =template.render({'posts':posts})
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
    html=template.render()
    return HttpResponse(html)

def bootstrap_test(request):
    template=get_template('test_base.html')
    html=template.render()
    return HttpResponse(html)

def listing(request):
    html='''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <title>中古機列表</title>
        </head>

        <body>
            <h2>以下是目前本店販售中的二手機列表</h2>
            <hr>
            <table width=400 border=1 bgcolor='#CCFFCC'>
            {}
            </table>
        </body>
        </html>
        '''
    products= Product.objects.all()
    tags= '<tr><td>品名</td><td>售價</td><td>庫存量</td></tr>'
    for p in products:
        tags= tags+ '<tr><td><a href=/list/'+p.sku+'>{}</a></td>'.format(p.name)
        tags= tags+ '<td>{}</td>'.format(p.price)
        tags= tags+ '<td>{}</td></tr>'.format(p.qty)
    return HttpResponse(html.format(tags))

def disp_detail(request, sku):
    html='''
        <!DOCTYPE html>
        <html>
        <head>
            <meta charset='utf-8'>
            <title>{}</title>
        </head>

        <body>
            <h2>{}</h2>
            <hr>
            <table width=400 border=1 bgcolor='#CCFFCC'>
            {}
            </table>
            <a href='/list'>回列表</a>
        </body>
        </html>
        '''
    try:
        p= Product.objects.get(sku=sku)
    except Product.DoesNotExist:
        raise Http404('找不到指定品項編號')

    tags= '<tr><td>品項編號</td><td>{}'.format(p.sku)
    tags=tags+'<tr><td>名稱</td><td>{}</td></tr>'.format(p.name)
    tags=tags+'<tr><td>售價</td><td>{}</td></tr>'.format(p.price)
    tags=tags+'<tr><td>數量</td><td>{}</td></tr>'.format(p.qty)
    return HttpResponse(html.format(p.name,p.name,tags))


