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





