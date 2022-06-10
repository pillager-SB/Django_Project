from django.contrib.auth import get_user_model
from django.db import models
from mainapp.models import Product


class Order(models.Model):
    CREATED = "CREATED"
    PAID = "PAID"
    SENT = "SENT"
    DELIVERED = "DELIVERED"
    CANCELED = "CANCELED"

    STATUS_CHOICES = [
        (CREATED, "Created"),
        (PAID, "Paid"),
        (SENT, "Sent"),
        (DELIVERED, "Delivered"),
        (CANCELED, "Canceled")
    ]
    user = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="orders"
    )
    status = models.CharField(choices=STATUS_CHOICES, max_length=16)
    created_at = models.DateTimeField(auto_now_add=True)


class OrderItemsManager(models.Manager):
    def quantity(self):
        return sum(item.quantity for item in self.all())

    def sum(self):
        return sum(item.product.price * item.quantity for item in self.all())


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveSmallIntegerField(verbose_name='количество', default=0)

    objects = OrderItemsManager()

    @property
    def cost(self):
        return self.quantity * self.product.price

    def __str__(self):
        return f'{self.product} - {self.quantity} шт.)'