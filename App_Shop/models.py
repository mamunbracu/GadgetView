from django.db import models

# Create your models here.


class Category(models.Model):
    title = models.CharField(max_length=50)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Categories'


class Product(models.Model):
    mainimage = models.ImageField(upload_to='product_pics')
    name = models.CharField(max_length=100)
    detailes = models.TextField(max_length=1000, verbose_name='Description')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    created = models.DateTimeField(auto_now_add=True)
    preview_text = models.TextField(max_length=200, verbose_name='Preview')
    price = models.FloatField()
    old_price = models.FloatField(default=0.00)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('-created',)