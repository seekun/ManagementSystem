from django.shortcuts import render, Http404, redirect, HttpResponse
from .models import ArtiInFo
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from fuzzywuzzy import fuzz
from .parsedb import updatedb
from .my_function import title, page_manager, select_double


def parse_paper(request, query=None, id=None):
    context = {}
    p = None
    all_papers = ArtiInFo.objects.all()
    for i in all_papers:
        if str(i.id) == id:
            old_col = i
    p = old_col
    mylist = zip(p.author, p.authors_number)
    Funding = zip(p.Funding_Agency, p.Grant_Number)
    JCR = zip(p.JCR_categorie, p.Rank_in_Category, p.Quartile_in_Category)
    context['JCR'] = JCR
    context['mylist'] = mylist
    context['Funding'] = Funding
    context['p'] = p
    return render(request, 'web/parse_paper.html', context)


# from django_auth_example.users.models import User


def paper(request, query=None):
    queryset_list = ArtiInFo.objects.all()
    find = []
    relate = {}
    for i in queryset_list:
        for q in query:
            if q:
                for a in i.author:
                    fuzz_number = fuzz.partial_ratio(q, a)
                    if fuzz_number >= 95:
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


# 对于不同的筛选条件, 可以根据情况设置fuzz值, 和fuzz筛选的方法 https://stackoverflow.com/questions/10383044/fuzzy-string-compfarison
def search(request):
    context = {}
    query = request.GET.get("q")
    query2 = request.GET.get("q2")
    select2 = request.GET.get("gender2")
    select = request.GET.get("gender")
    if query:
        if select == 'title':
            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)

            if find:
                find = page_manager(request, find)
                context['find'] = find
                context['query'] = query
                context['select'] = select
                context['query2'] = query2
                context['select2'] = select2
                return render(request, 'web/search_result.html', context)
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'author':

            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)
            if find:
                find = page_manager(request, find)
                context['find'] = find
                context['query'] = query
                context['select'] = select
                return render(request, 'web/search_result.html', context)
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'KeyWords_Plus':

            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)

            if find:
                find = page_manager(request, find)
                context['find'] = find
                context['query'] = query
                context['select'] = select
                return render(request, 'web/search_result.html', context)
            else:
                return render(request, 'web/search_nothing.html')

        elif select == 'periodical':
            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)

            if find:
                find = page_manager(request, find)
                context['find'] = find
                context['query'] = query
                context['select'] = select
                return render(request, 'web/search_result.html', context)
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'DOI':
            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)

            if find:
                find = page_manager(request, find)
                context['find'] = find
                context['query'] = query
                context['select'] = select
                return render(request, 'web/search_result.html', context)
            else:
                return render(request, 'web/search_nothing.html')
        elif select == 'year':
            queryset_list = ArtiInFo.objects.all()
            find = title(query, queryset_list)
            if query2:
                find = select_double(select2, query2, find)

            if find:
                find = page_manager(request, find)
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
        if request.POST.get("q"):
            query = []
            query.append(request.POST.get("q"))
            query.append(request.POST.get("q2"))
            query.append(request.POST.get("q3"))
            query.append(request.POST.get("q4"))
            return paper(request, query)
        # 开始的时候没有加return,直接调用paper视图函数,结果没有返回结果.
        if request.POST.get("p"):
            query = []
            query.append(request.POST.get("p"))
            query.append(request.POST.get("p2"))
            query.append(request.POST.get("p3"))
            query.append(request.POST.get("p4"))
            return parse_paper(request, query, request.POST.get("w"))
        if request.POST.get("id"):
            col = {}
            new_col = {}
            col['id'] = request.POST.get("id")
            col['title'] = request.POST.get("title")
            col['periodical'] = request.POST.get("periodical")
            col['volume'] = request.POST.get("volume")
            col['page'] = request.POST.get("page")
            col['DOI'] = request.POST.get("DOI")
            col['year'] = request.POST.get("year")
            col['body'] = request.POST.get("body")
            col['author_key_word'] = request.POST.get("author_key_word")
            col['Keywords_Plus'] = request.POST.get("Keywords_Plus")
            col['reprint_author'] = request.POST.get("reprint_author")
            col['reprint_author_address'] = request.POST.get("reprint_author_address")
            col['address'] = request.POST.get("address")
            col['email'] = request.POST.get("email")
            col['Funding_Agency'] = request.POST.get("Funding_Agency")
            col['Grant_Number'] = request.POST.get("Grant_Number")
            col['Fund_information'] = request.POST.get("Fund_information")
            col['ISSN'] = request.POST.get("ISSN")
            col['eISSN'] = request.POST.get("eISSN")
            print("111111", request.POST.get("volume"))
            new_col['$set'] = col
            old_col = {"id": request.POST.get("id")}
            updatedb(old_col, new_col)
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


from django.http import HttpResponse
from django.views.generic import View
from .utils import render_to_pdf  # created in step 4
from django.template.loader import get_template


class GeneratePDF(View):
    def get(self, request, *args, **kwargs):
    # def get(self, request):
        template = get_template('pdf/invoice.html')
        context = {
            "invoice_id": 123,
            "customer_name": "John Cooper",
            "amount": 1399.99,
            "today": "Today",
        }
        html = template.render(context)
        return HttpResponse(html)
        # pdf = render_to_pdf('pdf/invoice.html', context)
        # if pdf:
        #     response = HttpResponse(pdf, content_type='application/pdf')
        #     filename = "Invoice_%s.pdf" % ("12341231")
        #     content = "inline; filename='%s'" % (filename)
        #     download = request.GET.get("download")
        #     if download:
        #         content = "attachment; filename='%s'" % (filename)
        #     response['Content-Disposition'] = content
        #     return response
        # return HttpResponse("Not found")
