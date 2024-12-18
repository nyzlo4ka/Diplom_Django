# Импорт необходимых модулей из Django
from django import forms  # Модуль для работы с формами
from django.contrib.auth.forms import UserCreationForm  # Форма для создания нового пользователя
from django.contrib.auth.models import User  # Модель пользователя


# Форма для входа пользователя в систему
class LoginForm(forms.Form):
    username = forms.CharField(label='Username')  # Поле для ввода имени пользователя
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)  # Поле для ввода пароля с использованием защищенного виджета


# Форма для регистрации нового пользователя
class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)  # Поле для ввода электронной почты, обязательное для заполнения

    class Meta:
        model = User  # Указываем, что модель, с которой будет работа, - это User
        fields = ['username', 'email', 'password1', 'password2']  # Поля, которые будут использоваться в форме


# Форма для добавления книги в корзину
class CartAddBookForm(forms.Form):
    quantity = forms.IntegerField(min_value=1,
                                  initial=1)  # Поле для ввода количества книг, минимальное значение - 1, значение по умолчанию - 1
