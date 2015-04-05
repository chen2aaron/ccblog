#coding: utf-8
from django.shortcuts import render
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home (request):
    post_list = Article.objects.all()  #获取全部的Article对象
    return render(request, 'home.html', {'post_list' : post_list})

# def detail(request, my_args):
# 	post = Article.objects.all()[int(my_args)]
# 	str = ("title = %s, category = %s, date_time = %s, content = %s" % (post.title, post.category, post.date_time, post.content))

# 	return HttpResponse(str)

# def temp(request):
# 	return render(request, 'temp.html', {'current_time':datetime.now()})

# def bootstrap(request):
# 	return render(request, 'bootstrap.html', {'current_time':datetime.now()})
