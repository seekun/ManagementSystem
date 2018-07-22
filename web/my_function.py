from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fuzzywuzzy import fuzz
from .parsedb import updatedb


def title(query, queryset_list):
    find = []
    relate = {}
    for i in queryset_list:
        if query:
            fuzz_number = fuzz.partial_ratio(query, i.title)
            if fuzz_number >= 95:
                relate[i.id] = fuzz_number
    sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
    for i in sorted_relate:
        for j in queryset_list:
            if str(i[0]) == str(j.id):
                find.append(j)
    # context = {}
    # context['find'] = find
    # context['query'] = query
    # context['select'] = "title"
    return find


def author(query, queryset_list):
    find = []
    relate = {}
    for i in queryset_list:
        if query:
            for a in i.author:
                fuzz_number = fuzz.partial_ratio(query, a)
                if fuzz_number >= 95:
                    relate[i.id] = fuzz_number
    sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
    for i in sorted_relate:
        for j in queryset_list:
            if str(i[0]) == str(j.id):
                find.append(j)

    return find


def KeyWords_Plus(query, queryset_list):
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

    return find


def periodical(query, queryset_list):
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

    return find


def year(query, queryset_list):
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

    return find


def DOI(query, queryset_list):
    find = []
    relate = {}
    for i in queryset_list:
        if query:
            fuzz_number = fuzz.partial_ratio(query, i.DOI)
            if fuzz_number >= 100:
                relate[i.id] = fuzz_number
    sorted_relate = sorted(relate.items(), key=lambda kv: kv[1])
    for i in sorted_relate:
        for j in queryset_list:
            if str(i[0]) == str(j.id):
                find.append(j)
    return find


def page_manager(request, find):
    page_robot = Paginator(find, 6)
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
    return find


def select_double(select2, query2, find):
    if select2 == 'title':
        find = title(query2, find)
    elif select2 == 'author':
        find = author(query2, find)
    elif select2 == 'DOI':
        find = DOI(query2, find)
    elif select2 == 'year':
        find = year(query2, find)
    elif select2 == 'periodical':
        find = periodical(query2, find)
    elif select2 == 'KeyWords_Plus':
        find = KeyWords_Plus(query2, find)
    return find