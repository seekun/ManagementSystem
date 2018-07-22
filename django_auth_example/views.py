from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fuzzywuzzy import fuzz


def index(request):
    return render(request, 'index.html')

# 对于不同的筛选条件, 可以根据情况设置fuzz值, 和fuzz筛选的方法 https://stackoverflow.com/questions/10383044/fuzzy-string-comparison
def index_search(request):
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