from django.http import HttpResponse
from django.shortcuts import render
from login import models


# Create your views here.


# user_list = []  # 空列表


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # print(username, password)
        # temp = {'user': username, 'pwd': password}
        # user_list.append(temp)
        # 将数据保存到数据库
        models.UserInfo.objects.create(user=username, password=password)
    #从数据库中读取所有用户
    user_list = models.UserInfo.objects.all()

    # return HttpResponse('Hello World!')
    return render(request, 'login/index.html', {'data': user_list})
