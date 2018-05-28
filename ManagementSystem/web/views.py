from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):

    limit = 5
    queryset_list = ArtiInFo.objects.all()
    query = request.GET.get("q")
    find_paper = []
    for i in queryset_list:
        if query:
            if query in i.author:
               find_paper.append(i)

    paginator = Paginator(find_paper, limit)
    page = request.GET.get('page')
    try:
        contacts = paginator.page(page)
    except PageNotAnInteger:
        # 如果用户请求的页码号不是整数，显示第一页
        contacts = paginator.page(1)
    except EmptyPage:
        # 如果用户请求的页码号超过了最大页码号，显示最后一页
        contacts = paginator.page(paginator.num_pages)
    find = contacts
    return render(request, 'web/index.html', {'find': find})


def search(request):
    limit = 4
    queryset_list = ArtiInFo.objects.all()
    query = request.GET.get("q")
    find = []
    for i in queryset_list:
        if query:
            if query in i.title:
                find.append(i)

    paginator = Paginator(find, limit)
    page = request.GET.get('page', 1)
    loaded = paginator.page(page)
    context = {
        'find': loaded
    }
    return render(request, 'index.html', context)