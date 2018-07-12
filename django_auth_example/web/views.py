from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fuzzywuzzy import fuzz


# from django_auth_example.users.models import User


def paper(request, query=None):
    queryset_list = ArtiInFo.objects.all()
    # query = request.GET.get("q")
    find_paper = []
    for i in queryset_list:
        if query:
            for author in i.authors:
                if query in author:
                    find_paper.append(i)

    context = {}
    if query:
        queryset_list = ArtiInFo.objects.all()
        find = []
        for i in queryset_list:
            if query:
                if query in i.title:
                    find.append(i)

        # page_robot = Paginator(find, 5)
        # page = request.GET.get('page')
        # vids_list = page_robot.get_page(page)

        # try:
        #     vids_list = page_robot.get_page(page)
        # except PageNotAnInteger:
        #     # 如果用户请求的页码号不是整数，显示第一页
        #     vids_list = page_robot.get_page(1)
        # except EmptyPage:
        #     # 如果用户请求的页码号超过了最大页码号，显示最后一页
        #     vids_list = page_robot.get_page(vids_list.num_pages)
        # find = vids_list
        context['find'] = find
        context['query'] = query
        return render(request, 'web/index.html', context)
    else:
        return render(request, 'web/index.html')


def index(request):
    return render(request, 'web/index.html')


# 对于不同的筛选条件, 可以根据情况设置fuzz值, 和fuzz筛选的方法 https://stackoverflow.com/questions/10383044/fuzzy-string-comparison
def search(request):
    context = {}
    query = request.GET.get("q")
    select = request.GET.get("gender")
    if select == 'title':
        if query:
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.partial_ratio(query, i.title)
                    if fuzz_number >= 50:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            page_robot = Paginator(find, 5)
            page = request.GET.get('page')
            vids_list = page_robot.get_page(page)

            try:
                vids_list = page_robot.get_page(page)
            except PageNotAnInteger:
                # 如果用户请求的页码号不是整数，显示第一页
                vids_list = page_robot.get_page(1)
            except EmptyPage:
                # 如果用户请求的页码号超过了最大页码号，显示最后一页
                vids_list = page_robot.get_page(vids_list.num_pages)
            find = vids_list
            context['find'] = find
            context['query'] = query
            context['select'] = select
            return render(request, 'web/search_result.html', context)
    elif select == 'authors':
        if query:
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    for author in i.authors:
                        fuzz_number = fuzz.partial_ratio(query, author)
                        if fuzz_number >= 80:
                            relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)

            page_robot = Paginator(find, 5)
            page = request.GET.get('page')
            vids_list = page_robot.get_page(page)

            try:
                vids_list = page_robot.get_page(page)
            except PageNotAnInteger:
                # 如果用户请求的页码号不是整数，显示第一页
                vids_list = page_robot.get_page(1)
            except EmptyPage:
                # 如果用户请求的页码号超过了最大页码号，显示最后一页
                vids_list = page_robot.get_page(vids_list.num_pages)
            find = vids_list
            context['find'] = find
            context['query'] = query
            return render(request, 'web/search_result.html', context)
    elif select == 'Key_words_pluses':
        if query:
            queryset_list = ArtiInFo.objects.all()
            find = []
            # for i in queryset_list:
            #     if query:
            #         if query in i.Key_words_pluses:
            #             find.append(i)
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.token_set_ratio(query, i.Key_words_pluses)
                    if fuzz_number >= 90:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            page_robot = Paginator(find, 5)
            page = request.GET.get('page')
            vids_list = page_robot.get_page(page)

            try:
                vids_list = page_robot.get_page(page)
            except PageNotAnInteger:
                # 如果用户请求的页码号不是整数，显示第一页
                vids_list = page_robot.get_page(1)
            except EmptyPage:
                # 如果用户请求的页码号超过了最大页码号，显示最后一页
                vids_list = page_robot.get_page(vids_list.num_pages)
            find = vids_list
            context['find'] = find
            context['query'] = query
            return render(request, 'web/search_result.html', context)
    else:
        return render(request, 'web/search.html')


def profile(request):
    if request.method == 'POST':
        query = request.POST.get("q")
        return paper(request, query)
    # 开始的时候没有加return,直接调用paper视图函数,结果没有返回结果.

    return render(request, 'web/user_profile.html')


def detail(request, page_num):
    context = {}
    paper_detail = None
    all_papers = ArtiInFo.objects.all()
    for i in all_papers:
        if page_num == str(i['id']):
            paper_detail = i
    p = paper_detail
    context['p'] = p

    return render(request, 'web/detail.html', context)
