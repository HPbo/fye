# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render
from .models import UserInfo
def index(request):    
    # 每页显示2个记录
    paginator = Paginator(UserInfo.objects.all(), 2)
    page = request.GET.get('page')
    try:
        rows = paginator.page(page)
    except PageNotAnInteger:
        rows = paginator.page(1)
    except EmptyPage:
        rows = paginator.page(paginator.num_pages)
    return render(request, 'fye/index.html', {'result_list': rows})