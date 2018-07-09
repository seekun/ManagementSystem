from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def paper(request, query=None):
    print(query)
    limit = 5
    queryset_list = ArtiInFo.objects.all()
    # query = request.GET.get("q")
    find_paper = []
    for i in queryset_list:
        if query:
            if query in i.authors:
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


def index(request):
    return render(request, 'web/index.html')


def search(request):
    query = request.GET.get("q")
    if query:
        limit = 4
        queryset_list = ArtiInFo.objects.all()

        find = []
        for i in queryset_list:
            if query:
                if query in i.title:
                    find.append(i)

        paginator = Paginator(find, limit)
        page = request.GET.get('page', 1)
        find = paginator.page(page)
        context = {
            'find': find
        }
        return render(request, 'web/search_result.html', context)
    else:
        return render(request, 'web/search.html')


def profile(request):
    if request.method == 'POST':
        query = request.POST.get("q")

        return paper(request, query)
# 开始的时候没有加return,直接调用paper视图函数,结果没有返回结果.

    return render(request, 'web/user_profile.html')