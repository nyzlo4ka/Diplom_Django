# Импортируем необходимые модули из Django
from django.db import models  # Модуль для работы с моделями базы данных
from django.contrib.auth.models import User  # Импорт модели пользователя


# Модель книги
class Book(models.Model):
    author = models.CharField(max_length=100, db_collation='NOCASE')  # Поле для имени автора, максимальная длина - 100 символов
    title = models.CharField(max_length=100,
                             db_index=True, db_collation='NOCASE')  # Поле для названия книги, это поле индексируется для ускорения поиска
    genre = models.CharField(max_length=100, db_collation='NOCASE')  # Поле для жанра книги
    description = models.TextField()  # Поле для описания книги, без ограничения по количеству символов
    publish = models.CharField(max_length=100, db_collation='NOCASE')  # Поле для названия издательства
    year = models.IntegerField()  # Поле для года публикации книги
    pages = models.IntegerField()  # Поле для количества страниц в книге
    cost = models.DecimalField(max_digits=10, decimal_places=2)  # Поле для стоимости книги

    def __str__(self):
        return self.title  # Возвращает название книги при вызове экземпляра модели


# Модель корзины
class Cart(models.Model):
    user = models.OneToOneField(User,
                                on_delete=models.CASCADE)  # Связывает корзину с уникальным пользователем (один к одному), корзина будет удалена при удалении пользователя
    created_at = models.DateTimeField(
        auto_now_add=True)  # Поле для хранения даты и времени создания корзины, автоматически заполняется при создании


# Модель элемента корзины
class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items',
                             on_delete=models.CASCADE)  # Связывает элемент с корзиной, корзина будет удалена вместе с элементами при её удалении
    book = models.ForeignKey(Book, on_delete=models.CASCADE)  # Связывает элемент с книгой
    quantity = models.PositiveIntegerField(
        default=1)  # Поле для указания количества данной книги в корзине, по умолчанию - 1
