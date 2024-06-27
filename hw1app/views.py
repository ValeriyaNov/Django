from django.http import HttpResponse
import logging
import datetime
logger = logging.getLogger(__name__)


def index(request):
    text = '''<header class="header">
        <div class="nav">
            <a href="/" class="nav_item">Главная</a>
            <a href="/about/" class="nav_item">Обо мне</a>
            
        </div>
        <div class="title">
            <h1 class="title_text">Главная</h1>
        </div>
    </header>
    <div class="content">
            <h3 class="content_text">Это мой первый проект на Django! Пока еще рано судить) я только учусь)</h3>
        </div>
    '''
    now = datetime.datetime.today()
    logger.info(f'Site "Main" open in {now.strftime('%m/%d/%Y %H.%M.%S')}')
    return HttpResponse(text)
def about(request):
    text = '''<header class="header">
        <div class="nav">
            <a href="/" class="nav_item">Главная</a>
            <a href="/about/" class="nav_item">Обо мне</a>
            
        </div>
        <div class="title">
            <h1 class="title_text">Обо мне</h1>
        </div>
    </header>
    <div class="content">
            <h3 class="content_text">Добрый день! Меня зовут Валерия. Мне 29 лет. Живу в Москве. Работаю в сфере СИЗ</h3>

        </div>
    '''
    now = datetime.datetime.today()
    logger.info(f'Site "About us" open in {now.strftime('%m/%d/%Y %H.%M.%S')}')
    return HttpResponse(text)
