
# Приложение Django

### Не доработан

Это приложение представляет собой базовы проект интернет-магазина разработанный на Django. Оно позволяет пользователям просматривать книги и подробную информацию о них, искать по определенным параметрам,  регистрироваться и входить в систему, добавлять книги в свою корзину, а также просматривать/управлять ее содержимым.

# Структура проекта

![111](https://github.com/user-attachments/assets/0760d9e9-5a94-4b41-bca8-217f2f1c80fc)

![222](https://github.com/user-attachments/assets/d2d5e616-99a7-432f-99dc-d072ee433da2)

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

1. Скачайте исходный код репозитория и распакуйте его на свой компьютер.

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

Попадаем на ддомашнюю страницу, она отображает шаблон "app/home.html".

![1](https://github.com/user-attachments/assets/b4f516a2-0c3b-47d6-b180-3b688e9b5dd5)

read_books (Чтение книг): Извлекает все книги из базы данных, разбивает их на страницы по 10 шт и отображает шаблон "books_list.html" с информацией о страницах.

![5](https://github.com/user-attachments/assets/cb1c20b6-85ee-47ff-b4f2-2a749830bc7f)


get_searched_book (Поиск книги): Обрабатывает поиск книг на основе поисковых запросов в полях автора, названия, жанра или издательства. Отображает шаблон "search.html" с результатами поиска.

![6](https://github.com/user-attachments/assets/4bb0299d-a0b1-41a1-b7a1-ae19d6939c87)

Если ничего не найдено уведомляет об этом:

![10](https://github.com/user-attachments/assets/7a2ec7b6-ba7c-4c9d-931b-0d19063e00b6)

get_book_by_id (Получение книги по ID): Извлекает конкретную книгу по ее ID и отображает шаблон "book_detail.html" с подробной информацией о книге.

![7](https://github.com/user-attachments/assets/354ce2e2-1ae9-4152-8581-864acb8c9d27)


register_view (Представление регистрации): Обрабатывает регистрацию пользователя с помощью формы регистрации. Проверяет данные формы, создает нового пользователя и перенаправляет на страницу входа с сообщениями об успехе/ошибке.

![2](https://github.com/user-attachments/assets/d5aa59e0-6e41-4352-bf13-58f3663ae20e)


login_view (Представление входа): Обрабатывает попытки входа пользователя с помощью формы входа. Проверяет учетные данные, выполняет вход для успешных пользователей и перенаправляет на домашнюю страницу.

![3](https://github.com/user-attachments/assets/da8ddc41-485a-41be-936f-2e5a6faa28a4)
![4](https://github.com/user-attachments/assets/be76a8ca-ca1d-4416-b50f-b5bcb9f4748e)


logout_view (Выход из системы): Выполняет выход текущего пользователя из системы и перенаправляет на домашнюю страницу.


view_cart (Просмотр корзины): (Требуется вход пользователя) Извлекает корзину пользователя, вычисляет общую стоимость всех товаров и отображает шаблон "cart.html" с информацией о корзине и общей стоимостью.

add_to_cart (Добавить в корзину): (Требуется вход пользователя) Добавляет книгу (указанную по ID) в корзину пользователя. Обрабатывает создание корзины, если она не существует, и обновляет количество, если книга уже есть в корзине. Перенаправляет на просмотр корзины.

![8](https://github.com/user-attachments/assets/9f523865-a21f-4aa8-908c-1ed4b2a11a58)

remove_from_cart (Удалить из корзины): (Требуется вход пользователя) Удаляет определенную книгу из корзины пользователя и перенаправляет на просмотр корзины.

![9](https://github.com/user-attachments/assets/0a7b4189-8b3d-4a03-a3fd-6adfe25fb476)


## Команда проекта

- [Губарева Анна](https://github.com/nyzlo4ka)

## Источники
... 
