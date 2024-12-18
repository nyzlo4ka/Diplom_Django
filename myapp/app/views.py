import json  # Импортируем библиотеку для работы с JSON
from django.core.exceptions import ObjectDoesNotExist  # Исключение для обработки отсутствующих объектов
from django.db.models import Q  # Импортируем для выполнения сложных запросов к модели
from django.shortcuts import render, get_object_or_404, redirect  # Импортируем функции для обработки запросов
from .models import *  # Импортируем все модели из текущего приложения
from django.contrib.auth import authenticate, login, \
    logout  # Импортируем функции для работы с аутентификацией пользователя
from .forms import LoginForm, RegisterForm  # Импортируем формы для логина и регистрации
from django.contrib.auth.decorators import login_required  # Декоратор для ограничения доступа к представлениям


def load_books():  # Функция загрузки книг из файла books.json в базу данных
    try:
        with open('books.json', encoding='utf-8') as f:  # Открывает файл для чтения
            books_data = json.load(f)  # Загружает данные из файла в словарь
            for book_data in books_data:
                book_id = book_data['id']  # Получаем ID книги
                try:
                    Book.objects.get(id=book_id)  # Проверяем, существует ли книга в базе
                except ObjectDoesNotExist:  # Если книга не найдена
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
                    book.save()  # Сохраняем новую книгу в базе данны
    except Exception as e:
        print(f"Ошибка при загрузке книг: {e}")  # Обработка ошибок при загрузке


load_books()  # Загружаем книги при старте приложения


def home_page(request):  # Представление для домашней страницы
    return render(request, 'app/home.html')  # Отображение шаблона домашней страницы


def read_books(request):  # Представление для чтения всех книг
    books = Book.objects.all()  # Получаем все книги из базы данных
    return render(request, 'app/books_list.html', {'books': books})  # Отображаем список


def get_book_by_id(request, book_id):  # Представление для получения книги по её ID
    book = get_object_or_404(Book, id=book_id)  # Получаем книгу или 404 ошибку если не найдено
    return render(request, 'app/book_detail.html', {'book': book})  # Отображаем детали книги


def get_searched_book(request):  # Представление для поиска книг
    query = request.GET.get('query', '')  # Получаем поисковой запрос
    books = []  # Инициализацию списка для найденных книг
    if query:
        books = Book.objects.filter(
            Q(author__icontains=query) | Q(title__icontains=query) |
            Q(genre__icontains=query) | Q(publish__icontains=query) | Q(cost__icontains=query)
        )  # Поиск книг по различным критериям
    return render(request, 'app/search.html', {'books': books, 'query': query})
    # Отображение результатов поиска


def login_view(request):  # Представление для входа пользователей
    if request.method == 'POST':
        form = LoginForm(request.POST)  # Создаем форму с данными запроса
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)  # Проверяем пользователя
            if user is not None:
                login(request, user)  # Логиним пользователя
                return redirect('home')  # Перенаправляем на домашнюю страницу
    else:
        form = LoginForm()  # Если POST не успешен, создаем пустую форму
    return render(request, 'app/login.html', {'form': form})  # Отображаем форму входа


# Представление для регистрации пользователей
def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)  # Создаем форму с данными запроса
        if form.is_valid():
            form.save()  # Сохраняем нового пользователя в базе данных
        return redirect('login')  # Перенаправляем на страницу логина
    else:
        form = RegisterForm()  # Если POST не успешен, создаем пустую форму
    return render(request, 'app/register.html', {'form': form})  # Отображаем форму регистрации


# Представление для выхода пользователя
def logout_view(request):
    logout(request)  # Выход пользователя из системы
    return redirect('login')  # Перенаправляем на страницу логина


# Представление для добавления книги в корзину, требует авторизации
@login_required
def add_to_cart(request, book_id):
    book = get_object_or_404(Book, id=book_id)  # Получаем книгу или 404 ошибку если не найдено
    cart, created = Cart.objects.get_or_create(user=request.user)  # Получаем корзину пользователя или создаем новую
    cart_item, created = CartItem.objects.get_or_create(cart=cart,
                                                        book=book)  # Получаем элемент корзины или создаем новый
    if created:
        cart_item.quantity = 1  # Если это новый элемент, устанавливаем количество 1
    else:
        cart_item.quantity += 1  # Если элемент уже существует, увеличиваем количество на 1
    cart_item.save()  # Сохраняем изменения в элементе корзины
    return redirect('view_cart')  # Перенаправляем на страницу с корзиной


# Представление для просмотра содержимого корзины, требует авторизации
@login_required
def view_cart(request):
    cart = get_object_or_404(Cart, user=request.user)  # Получаем корзину пользователя или 404 ошибку если не найдено
    return render(request, 'app/cart.html', {'cart': cart})  # Отображаем содержимое корзины
