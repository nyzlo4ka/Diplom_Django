
# Приложение Django

Этот код представляет собой проект интернет-магазина, разработанный на Django.

# Структура проекта

myapp/

├── myapp/

│   ├── __init__.py

│   ├── settings.py

│   ├── urls.py

│   ├── wsgi.py

│   └── asgi.py

├── app/

│   ├── __init__.py

│   ├── admin.py

│   ├── apps.py

│   ├── forms.py

│   ├── models.py

│   ├── views.py

│   ├── tests.py

│   ├── urls.py

│   └── migrations/

│       └── __init__.py

├── templates/

│   └── app/

│       ├── base.html

│       ├── book_detail.html

│       ├── books_list.html

│       ├── cart.html

│       ├── home.html

│       ├── login.html

│       ├── register.html

│       └── search.html

├── books.json

├── db.db

├── manage.py

├── manage.py

└── req.txt


## Содержание
- [Технологии](#технологии)
- [Установка и использование]()
- [Команда проекта](#команда-проекта)

## Технологии
- Django
- SQL
- HTML
- JSON
- Python

## Установка и использование

Для установки и запуска проекта, необходим Python 3.12.

1. Скачайте исходный код репозитория в ZIP-архиве и распакуйте его на свой компьютер.

2. Создайте виртуальное окружение и активируйте его
```
python -m venv venv

venv\Scripts\activate
```
3. Установите зависимости
```
pip install -r req.txt
```
4. Запустите миграции и загрузите данные в БД
```
python manage.py makemigrations 

python manage.py migrate
```
5. Запустите сервер
```
python manage.py runserver
```
Откройте браузер и перейдите по адресу http://127.0.0.1:8000/.


### Дипломный проект часть 3


## Команда проекта

- [Губарева Анна](https://github.com/nyzlo4ka) — Front-End Engineer

## Источники
... 