# -*- coding:utf-8 -*-

from rest_framework.pagination import PageNumberPagination

"""
自定义分页器, 默认10条
"""


class BasePagination(PageNumberPagination):
    page_size = 10  # 每页显示多少条数据
    page_query_param = "page"  # 127.0.0.1:8000/books/?page=5 查询第5页
    page_size_query_param = "limit"  # 前台控制每页显示的最大条数
    max_page_size = 50  # 后台控制显示的最大记录条数，防止前台输入的查询条数过大