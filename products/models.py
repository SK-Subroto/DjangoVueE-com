from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    class Meta:
        verbose_name = 'Categorie'

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=255, null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    img = models.ImageField(blank=True, null=True)
    name = models.CharField(max_length=255, null=True)
    category = models.ForeignKey(Category, related_name='products', null=True, on_delete=models.CASCADE)
    supplier = models.ForeignKey(Supplier, null=True, on_delete=models.CASCADE)
    price = models.IntegerField(null=True)
    description = models.TextField(null=True)

    def __str__(self):
        return self.name

    @property
    def category_name(self):
        return self.category.name

    @property
    def supplier_name(self):
        return self.supplier.name