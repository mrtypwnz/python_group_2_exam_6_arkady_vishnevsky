from django.contrib.auth.models import User
from django.db import models

GENDER_CHOICES = [
    ['male', "Мужской"],
    ['female', "Женский"],
]

class UserInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT, verbose_name="Пользователь")
    avatar = models.FileField(null=True, blank=True, verbose_name="Аватар")
    birth_date = models.DateField(null=True, blank=True, verbose_name="Дата рождения")
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default="male", verbose_name="Пол")
    phone_number = models.CharField(max_length=15, verbose_name="Номер телефона")
    friends = models.ManyToManyField(User, blank=True, related_name='friends', verbose_name='Друзья')

class Post(models.Model):
    title = models.CharField(max_length=100, verbose_name='Заголовок')
    text = models.TextField(max_length=10000, verbose_name='Текст')
    article_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.PROTECT, related_name='Посты', verbose_name='Автор')





