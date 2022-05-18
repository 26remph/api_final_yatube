![](./yatube_api/static/header.png)

[//]: # (#API для проекта Yatube)

Финальная версия API, в которой применены все знания теоретической части по теме
django-rest-framework. [Yatube](http://vidim.pythonanywhere.com/) - это социальная сеть для публикации своих постов. Поддерживает разные тематические группы. Авторство и подписки.  
___
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)

![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/26remph/api_final_yatube)
![GitHub repo size](https://img.shields.io/github/repo-size/26remph/api_final_yatube)
![GitHub](https://img.shields.io/github/license/26remph/api_final_yatube)
![pythonversion](https://img.shields.io/badge/python-%3E%3D3.7-blue)

##Оглавление
0. [Как запустить проект](#как-запустить-проект)
1. [Документация по api для yatoube](#документация-по-api)
2. [Об авторе](#об-авторе)
3. [Контрольная сумма репозитария](#контрольная-сумма-проекта)

###Как запустить проект  
Клонировать репозиторий и перейти в него в командной строке:

`git clone https://github.com/yandex-praktikum/kittygram.git`  
`cd kittygram`  

Cоздать и активировать виртуальное окружение:  
`python3 -m venv env`
`source env/bin/activate`

Установить зависимости из файла requirements.txt:  
`python3 -m pip install --upgrade pip`
`pip install -r requirements.txt`

Выполнить миграции:
`python3 manage.py migrate`  
Запустить проект:
`python3 manage.py runserver`

###Документация по API

Когда вы запустите проект, по адресу `http://127.0.0.1:8000/redoc/` будет доступна документация для **API Yatube**.  
Документация представлена в формате [Redoc](https://github.com/Redocly/redoc).

###Об авторе
Вадим Барсуков,  
студент 33 когорты,  
Яндекс Практикум  
:e-mail:  
v.bars@vidim.ru

###Контрольная сумма репозитария
`SHA-1: ab09e0fb0ed739ce2a5d5c28eb49db1b2834dbcf`
<br>
<br>
<br>
<br>
<br>
___
<p>
    <img align="center" src="./yatube_api/static/fav.svg" title="home page"/>
    <span>© 2022, Vidim, Inc., temet nosce ツ </span>
</p>