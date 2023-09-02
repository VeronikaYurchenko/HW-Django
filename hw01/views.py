import logging

from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

logger = logging.getLogger(__name__)

headers = {'Cache-Control': 'no-cache, must-revalidate',
           'Pragma': 'no-cache'}


def index(reqwest):   # hw01/index/
    body = """
    <h1>Главная страница</h1>
    <p>Содержимое главной страницы</p>
    """
    logger.info(f'Страница открыта')
    return HttpResponse(body, charset="utf-8", headers=headers)


def about(reqwest):  # hw01/about/
    body = """
        <h1>О себе</h1>
        <p>Содержимое страницы о себе</p>
        """
    logger.info(f'Страница открыта')
    return HttpResponse(body, charset="utf-8", headers=headers)