from django.urls import path
from . import views  # импортируем представления (views) из текущего приложения

urlpatterns = [
    # Главная страница приложения, отображает домашнюю страницу
    path('', views.home_page, name='home'),

    # Страница для просмотра всех книг, использует представление read_books
    path('books/', views.read_books, name='read_books'),

    # Страница отображения информации о конкретной книге по ее ID, использует представление get_book_by_id
    path('books/<int:book_id>/', views.get_book_by_id, name='get_book_by_id'),

    # Страница для поиска книг, использует представление get_searched_book
    path('search/', views.get_searched_book, name='search'),

    # Страница для входа в систему, использует представление login_view
    path('login/', views.login_view, name='login'),

    # Страница для регистрации нового пользователя, использует представление register_view
    path('register/', views.register_view, name='register'),

    # Страница для выхода из системы, использует представление logout_view
    path('logout/', views.logout_view, name='logout'),

    # Страница для просмотра содержимого корзины, использует представление view_cart
    path('cart/', views.view_cart, name='view_cart'),

    # URL для добавления книги в корзину, использует представление add_to_cart с параметром book_id
    path('cart/add/<int:book_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:book_id>/', views.remove_from_cart, name='remove_from_cart'),

]
