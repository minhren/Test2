from django.shortcuts import render, redirect
from booktest.models import BookInfo, HeroInfo, AreaInfo
from datetime import date
from django.template import loader
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.


def index(request):
    """显示图书信息"""
    # 1 查找图书
    books = BookInfo.objects.all()
    return render(request, 'booktest/index.html', {'books': books})

    # books = BookInfo.objects.all()
    # # hero = book.heroinfo_set.all()
    # template = loader.get_template("booktest/index.html")
    # html = template.render({'books': books})
    # return HttpResponse(html)


def create(request):
    b = BookInfo()
    b.btitle = "流星蝴蝶剑"
    b.bpub_date = date(1999, 5, 5)
    b.save()
    return HttpResponseRedirect(redirect_to='/index')


def delete(request, bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    # return HttpResponseRedirect(redirect_to='/index')
    return redirect('/index')


def areas(request):
    city = AreaInfo.objects.get(title='广州市')
    parent = city.parent
    children = city.areainfo_set.all()
    return render(request, 'booktest/areas.html', {'city': city, 'parent': parent, 'children': children})


def login_check(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username == 'admin':
        # print("ok")
        return redirect('/index')
        # return HttpResponse("ok")
    else:
        print("error")
        return redirect(to='/login')
        # return HttpResponse('password error')


def login(request):
    return render(request, 'booktest/login.html', {})
