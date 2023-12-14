from django.contrib.auth.models import User
from django.db import models


class Product(models.Model):
    name = models.CharField(max_length=100)
    composition = models.TextField()
    price = models.DecimalField(decimal_places=2, max_digits=7)
    available = models.PositiveSmallIntegerField()
    last_delivery = models.DateTimeField()
    age_restricted = models.BooleanField()

    def __str__(self):
        ava = f'В наличии {self.available} штук' if self.available > 0 else 'Нет в наличии'
        age = '18+' if self.age_restricted else ''

        return f'{self.name} - {ava} - {age}'


class Order(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.customer} - {self.date}'


class OrderProducts(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    count = models.IntegerField()

    def __str__(self):
        return f'{self.order.customer} - {self.product.name} - {self.count} штук'