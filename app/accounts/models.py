from django.contrib.auth import get_user_model
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


class Profile(models.Model):
    user = models.OneToOneField(get_user_model(), related_name='profile', on_delete=models.CASCADE, verbose_name='Пользователь')
    avatar = models.ImageField(null=True, blank=True, upload_to='uploads/avatars', verbose_name='Аватар')
    about = models.TextField(null=True, blank=True, verbose_name='О пользователе')
    phone = PhoneNumberField(blank=True, verbose_name='Телефон')

    def __str__(self):
        return "Профиль" + " " + self.user.get_full_name()

    class Meta:
        verbose_name = 'Профиль'
        verbose_name_plural = 'Профили'
