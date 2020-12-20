from django.db import models
from django.conf import settings

#model
from App_Shop.models import Product
# Create your models here.


class Cart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='items')
    quantity = models.IntegerField(default=1)
    purchase = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.quantity} X {self.items}'
    
    def get_total(self):
        total = self.items.price * self.quantity
        float_total = format(total, '0.2f')
        return float_total

class Order(models.Model):
    orderitems = models.ManyToManyField(Cart)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ordered = models.BooleanField(default=False)
    paymentId = models.CharField(max_length=264, blank=True, null=True)
    orderId = models.CharField(max_length=264, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def get_totals(self):
        total = 0
        for order_item in self.orderitems.all():
            total += float(order_item.get_total())
        return total
    def get_cart_items(self):
        orderitem = self.orderitems.all()
        total = sum([item.quantity for item in orderitem])
        return total
