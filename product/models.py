from django.contrib.auth import get_user_model
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.core.mail import send_mail
from django.template.loader import render_to_string

User = get_user_model()


class Category(models.Model):
    title = models.SlugField(primary_key=True, unique=True)


class Product(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='products')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    title = models.CharField(max_length=50)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    image = models.ImageField(upload_to='images/')

    # def save(self):
    #     print('hellow')
    #     return super().save()


@receiver(post_save, sender=Product)
def product_post_save(sender, instance, created, **kwargs):
    if created:
        instance.price += 100
        instance.save(update_fields=['price'])

        send_mail(
            'Hello',
            '',
            'e352709@gmail.com',
            ['e352709@gmail.com'],
            html_message=render_to_string('send_mail.html', {'name': instance.title, 'price': instance.price})
        )