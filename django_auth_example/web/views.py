from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fuzzywuzzy import fuzz


# from django_auth_example.users.models import User


def paper(request, query=None):
    queryset_list = ArtiInFo.objects.all()
    find_paper = []
    # for i in queryset_list:
    #     for q in query:
    #         if q:
    #             for a in i.author:
    #                 if q in a:
    #                     find_paper.append(i)
    #
    # context = {}
    # if query:
    #     queryset_list = ArtiInFo.objects.all()
    #     find = []
    #     for i in queryset_list:
    #         if query:
    #             if query in i.title:
    #                 find.append(i)
    #
    #     context['find'] = find
    #     context['query'] = query
    # context['select'] = select
    print(query)
    queryset_list = ArtiInFo.objects.all()
    find = []
    relate = {}
    for i in queryset_list:
        for q in query:
            if q:
                for a in i.author:
                    fuzz_number = fuzz.partial_ratio(q, a)
                    if fuzz_number >= 90:
                        relate[i.id] = fuzz_number
    sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
    for i in sorted_relate:
        for j in queryset_list:
            if str(i[0]) == str(j.id):
                find.append(j)
    if find:
        context = {}
        context['find'] = find
        context['query'] = query
        return render(request, 'web/search_user_paper.html', context)

    else:
        return render(request, 'web/search_nothing.html')


# else:
# return render(request, 'web/search_user_paper.html')


def index(request):
    return render(request, 'web/search_user_paper.html')


# 对于不同的筛选条件, 可以根据情况设置fuzz值, 和fuzz筛选的方法 https://stackoverflow.com/questions/10383044/fuzzy-string-comparison
def search(request):
    context = {}
    query = request.GET.get("q")
    select = request.GET.get("gender")
    if query:
        if select == 'title':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.partial_ratio(query, i.title)
                    if fuzz_number >= 80:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            if find:
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
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'author':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    for a in i.author:
                        fuzz_number = fuzz.partial_ratio(query, a)
                        if fuzz_number >= 80:
                            relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)

            if find:
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
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'KeyWords_Plus':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    for a in i.KeyWords_Plus:
                        fuzz_number = fuzz.partial_ratio(query, a)
                        if fuzz_number >= 80:
                            relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            if find:
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
            else:
                return render(request, 'web/search_nothing.html')

        elif select == 'periodical':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.partial_ratio(query, i.periodical)
                    if fuzz_number >= 90:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            if find:
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
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'DOI':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.partial_ratio(query, i.DOI)
                    if fuzz_number >= 90:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            if find:
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
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'year':
            queryset_list = ArtiInFo.objects.all()
            find = []
            relate = {}
            for i in queryset_list:
                if query:
                    fuzz_number = fuzz.partial_ratio(query, i.year)
                    if fuzz_number >= 100:
                        relate[i.id] = fuzz_number
            sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
            for i in sorted_relate:
                for j in queryset_list:
                    if str(i[0]) == str(j.id):
                        find.append(j)
            if find:
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
            else:
                return render(request, 'web/search_nothing.html')

    else:
        return render(request, 'web/search.html')


def profile(request):
    if request.method == 'POST':
        query = []
        query.append(request.POST.get("q"))
        query.append(request.POST.get("q2"))
        query.append(request.POST.get("q3"))
        query.append(request.POST.get("q4"))
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
    mylist = zip(p.author, p.authors_number)
    Funding = zip(p.Funding_Agency, p.Grant_Number)
    JCR = zip(p.JCR_categorie, p.Rank_in_Category, p.Quartile_in_Category)
    context['JCR'] = JCR
    context['mylist'] = mylist
    context['Funding'] = Funding
    context['p'] = p
    return render(request, 'web/detail.html', context)


def introduce(request):
    return render(request, 'web/introduce.html')


def contact(request):
    return render(request, 'web/contact.html')
