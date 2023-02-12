# pastebin
___
![python_version](https://img.shields.io/badge/python-3.11-orange)
![django_version](https://img.shields.io/badge/django-4.1-orange)
![drf_version](https://img.shields.io/badge/django--rest--framework-3.14-orange)
![pygments_version](https://img.shields.io/badge/pygments-2.14-orange)

Пример веб-API которое позволяет загружать фрагменты исходного кода, для возможности просмотра окружающими.
![demo](demo.jpg)
___
Настройка перед запуском
___
Первое, что нужно сделать, это cклонировать репозиторий:

$ git clone https://github.com/Andrei2020-web/pastebin_api.git

$ cd pastebin_api

Создайте виртуальную среду для установки зависимостей и активируйте ее:

$ virtualenv venv

$ source venv/bin/activate

Затем установите зависимости:

(venv)$ pip install -r requirements.txt

Запускаем сервер:

(venv)$ python manage.py runserver
