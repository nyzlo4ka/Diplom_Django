import json  # Импортируем модуль для работы с JSON
from django.contrib import messages  # Импортируем модуль для работы с сообщениями
from django.core.exceptions import ObjectDoesNotExist  # Импортируем исключение для обработки отсутствующих объектов
from django.db.models import Q  # Импортируем Q для создания сложных запросов к базе данных
from django.shortcuts import render, get_object_or_404, redirect  # Импортируем функции для обработки запросов
from .models import *  # Импортируем все модели из текущего приложения
from django.contrib.auth import authenticate, login, logout  # Импортируем функции для аутентификации пользователей
from .forms import LoginForm, RegisterForm  # Импортируем формы для входа и регистрации
from django.contrib.auth.decorators import login_required  # Импортируем декоратор для защиты представлений
from django.core.paginator import Paginator  # Импортируем класс для постраничного отображения


def load_books():
    """Загружает книги из файла books.json в базу данных."""
    try:
        # Открываем файл books.json с кодировкой UTF-8
        with open('books.json', encoding='utf-8') as f:
            books_data = json.load(f)  # Загружаем данные из JSON-файла
            for book_data in books_data:  # Проходим по каждому элементу в загруженных данных
                book_id = book_data['id']  # Получаем идентификатор книги
                try:
                    # Проверяем, существует ли книга с данным идентификатором
                    Book.objects.get(id=book_id)
                except ObjectDoesNotExist:
                    # Если книга не найдена, создаем новый объект книги
                    book = Book(
                        id=book_id,
                        author=book_data['автор'],
                        title=book_data['название'],
                        genre=book_data['жанр'],
                        description=book_data['описание'],
                        publish=book_data['издательство'],
                        year=book_data['год публикации'],
                        pages=book_data['Количество страниц'],
                        cost=book_data['Цена'],
                    )
                    book.save()  # Сохраняем книгу в базе данных
    except Exception as e:
        # Обрабатываем любые исключения и выводим сообщение об ошибке
        print(f"Ошибка при загрузке книг: {e}")


load_books()  # Вызываем функцию для загрузки книг при старте приложения


def home_page(request):
    """Отображает главную страницу приложения."""
    return render(request, 'app/home.html')  # Рендерим шаблон главной страницы


def read_books(request):
    """Отображает список книг с постраничной навигацией."""
    books_list = Book.objects.all()  # Получаем все книги из базы данных
    books_per_page = 7  # Устанавливаем количество книг на странице
    paginator = Paginator(books_list, books_per_page)  # Создаем объект пагинатора
    page_number = request.GET.get('page')  # Получаем номер страницы из GET-запроса
    books = paginator.get_page(page_number)  # Получаем книги для текущей страницы
    return render(request, 'app/books_list.html',
                  {'books': books, 'books_per_page': books_per_page})  # Рендерим шаблон со списком книг


def get_searched_book(request):
    # Получаем строку запроса 'query' из GET-параметров, если она не указана, устанавливаем пустую строку
    query = request.GET.get('query', '')

    # Фильтруем книги по автору, названию, жанру или издательству, если 'query' не пустая
    books = Book.objects.filter(
        Q(author__icontains=query.capitalize()) |  # Поиск по автору (независимо от регистра)
        Q(title__icontains=query) |  # Поиск по названию (независимо от регистра)
        Q(genre__icontains=query) |  # Поиск по жанру (независимо от регистра)
        Q(publish__icontains=query)  # Поиск по издательству (независимо от регистра)
    ).distinct() if query else []  # Убираем дубликаты, если есть результаты, иначе возвращаем пустой список

    # Отправляем результаты поиска и сам запрос в шаблон 'search.html'
    return render(request, 'app/search.html', {'books': books, 'query': query})


def get_book_by_id(request, book_id):
    # Получаем книгу по ее идентификатору, если книга не найдена, возвращаем 404 ошибку
    book = get_object_or_404(Book, id=book_id)

    # Отправляем найденную книгу в шаблон 'book_detail.html'
    return render(request, 'app/book_detail.html', {'book': book})


def login_view(request):
    # Проверяем, был ли запрос методом POST (т.е. отправлена ли форма)
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Создаем форму с данными из POST-запроса
        if form.is_valid():  # Проверяем, валидна ли форма
            username = form.cleaned_data['username']  # Получаем имя пользователя
            password = form.cleaned_data['password']  # Получаем пароль
            user = authenticate(request, username=username, password=password)  # Аутентификация пользователя
            if user is not None:  # Если аутентификация успешна
                login(request, user)  # Входим в систему
                return redirect('home')  # Перенаправляем на главную страницу
    else:
        form = LoginForm()  # Если не POST, создаем пустую форму
    # Отправляем форму в шаблон 'login.html'
    return render(request, 'app/login.html', {'form': form})


def register_view(request):
    # Проверяем, был ли запрос методом POST (т.е. отправлена ли форма регистрации)
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Создаем форму с данными из POST-запроса
        if form.is_valid():  # Проверяем, валидна ли форма
            form.save()  # Сохраняем нового пользователя
            messages.success(request, "Регистрация прошла успешно! Вы можете войти.")  # Успешное сообщение
            return redirect('login')  # Перенаправляем на страницу входа
        else:
            messages.error(request, "Ошибка при регистрации. Пожалуйста, исправьте ошибки ниже.")  # Сообщение об ошибке
    else:
        form = RegisterForm()  # Если не POST, создаем пустую форму
    # Отправляем форму в шаблон 'register.html'
    return render(request, 'app/register.html', {'form': form})


def logout_view(request):
    # Выходим из системы
    logout(request)
    # Перенаправляем на главную страницу
    return redirect('home')


@login_required(login_url='login')
def add_to_cart(request, book_id):
    # Получаем книгу по ее идентификатору, если книга не найдена, возвращаем 404 ошибку
    book = get_object_or_404(Book, id=book_id)

    # Получаем или создаем корзину для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Получаем или создаем элемент корзины для данной книги
    cart_item, created = CartItem.objects.get_or_create(cart=cart, book=book)

    # Если элемент корзины был создан, устанавливаем количество в 1
    if created:
        cart_item.quantity = 1
    else:
        # Если элемент уже существует, увеличиваем его количество на 1
        cart_item.quantity += 1

    # Сохраняем изменения в элементе корзины
    cart_item.save()

    # Перенаправляем пользователя на страницу просмотра корзины
    return redirect('view_cart')


@login_required(login_url='login')
def view_cart(request):
    # Получаем или создаем корзину для текущего пользователя
    cart, created = Cart.objects.get_or_create(user=request.user)

    # Если в корзине нет элементов, отображаем пустую корзину
    if not cart.items.exists():
        return render(request, 'app/cart.html', {'cart': cart, 'items_with_price': [], 'total_price': 0})

    total_price = 0
    items_with_price = []

    # Проходим по всем элементам корзины и вычисляем общую стоимость
    for item in cart.items.all():
        item_total = item.book.cost * item.quantity  # Общая стоимость для данного элемента
        total_price += item_total  # Добавляем к общей стоимости
        items_with_price.append({
            'book': item.book,
            'title': item.book.title,
            'quantity': item.quantity,
            'price': item.book.cost,
            'item_total': item_total
        })

    # Отправляем данные о корзине и ее содержимом в шаблон 'cart.html'
    return render(request, 'app/cart.html',
                  {'cart': cart, 'total_price': total_price, 'items_with_price': items_with_price})


@login_required(login_url='login')
def remove_from_cart(request, book_id):
    # Получаем корзину для текущего пользователя, если не найдена, возвращаем 404 ошибку
    cart = get_object_or_404(Cart, user=request.user)

    # Получаем элемент корзины по идентификатору книги, если не найден, возвращаем 404 ошибку
    cart_item = get_object_or_404(CartItem, cart=cart, book__id=book_id)

    # Удаляем элемент из корзины
    cart_item.delete()

    # Перенаправляем пользователя на страницу просмотра корзины
    return redirect('view_cart')
