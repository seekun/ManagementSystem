from django.shortcuts import render, redirect, render_to_response
from .forms import RegisterForm, UserForm
from django.http import HttpResponse
import json
from django.template import RequestContext


def index(request):
    return render(request, 'index.html')


def register(request):
    redirect_to = request.POST.get('next', request.GET.get('next', ''))

    # 只有当请求为 POST 时，才表示用户提交了注册信息
    if request.method == 'POST':
        # request.POST 是一个类字典数据结构，记录了用户提交的注册信息
        # 这里提交的就是用户名（username）、密码（password）、邮箱（email）
        # 用这些数据实例化一个用户注册表单
        form = RegisterForm(request.POST)

        # 验证数据的合法性
        if form.is_valid():
            # 如果提交数据合法，调用表单的 save 方法将用户数据保存到数据库
            form.save()

            # 注册成功，跳转回首页
            if redirect_to:
                return redirect(redirect_to)
            else:
                return redirect('/')
    else:
        # 请求不是 POST，表明用户正在访问注册页面，展示一个空的注册表单给用户
        form = RegisterForm()

    # 渲染模板
    # 如果用户正在访问注册页面，则渲染的是一个空的注册表单
    # 如果用户通过表单提交注册信息，但是数据验证不合法，则渲染的是一个带有错误信息的表单
    return render(request, 'users/register.html', context={'form': form})


def profile(request):
    return render(request, 'web/user_profile.html')


def edit_profile(request):
    # try:
    #     profile = request.users_user.username
    # except User.DoesNotExist:
    #     profile = User()
    # instance = get_object_or_404(User, user_number=user_number)
    # form = UserForm(request.POST or None, instance=instance)
    if request.method == 'GET':
        form = UserForm(instance=request.user)
        # form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST, instance=request.user)
        if form.is_valid():
            # user_number = form.cleaned_data['user_number']
            # chinese_name = form.cleaned_data['chinese_name']
            # english_name = form.cleaned_data['english_name']
            # department = form.cleaned_data['department']
            #
            # new_profile = User(user_number=user_number, chinese_name=chinese_name, english_name=english_name,
            #                    department=department)
            # 需要加表单校验, 工号不能重复
            # english_name = {'a': 1, 'b': 2}
            # form.english_name = json.dumps(english_name)
            form.save()

            return redirect(to='/web/profile/')

    # context = {}
    # user_list = User.objects.all()
    # context['user_list'] = user_list
    # context['form'] = form
    context = {'form': form}
    return render(request, 'web/change.html', context)
