import django
from django.db import models


class Client:
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=254)
    phone = models.IntegerField(max_length=20)
    address = models.CharField(max_length=200)
    create_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, email: {self.email}, phone: {self.phone}, address: {self.address}'


class Goods:
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=200)
    price = models.IntegerField()
    amount = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'name: {self.name}, description: {self.description}, price: {self.price}, amount: {self.amount}'


class Order:
    price = models.IntegerField()
    create_at = models.DateField(auto_now_add=True)
    client_id = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internet_shop.client')
    goods_id = models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='internet_shop.goods')

    def __str__(self):
        return f'price: {self.price}, client_id: {self.client_id}, goods_id: {self.goods_id}'
