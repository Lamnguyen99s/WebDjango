from django.db import models
from Category.models import Category
# Create your models here.

class Product(models.Model):
    productName = models.CharField(max_length = 100)
    productCode = models.CharField(max_length = 20)
    productPrice = models.DecimalField(max_digits = 10, decimal_places = 3)
    productTitle = models.CharField(max_length = 500)
    productSize = models.CharField(max_length = 100)
    productDescription = models.TextField()
    productImg1 = models.ImageField(upload_to='uploads/products/')
    productImg2 = models.ImageField(upload_to='uploads/products/')
    productImg3 = models.ImageField(upload_to='uploads/products/')
    productImg4 = models.ImageField(upload_to='uploads/products/')
    categoryID = models.ForeignKey(Category, on_delete = models.CASCADE)
    
    def __str__(self):
        return self.productName
    
    class Meta:
        db_table = 'product'
    