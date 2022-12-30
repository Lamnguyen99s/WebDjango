from django.db import models

# Create your models here.
class Category(models.Model):
    categoryName = models.CharField(max_length = 100)
    categoryCode = models.CharField(max_length = 20)
    categoryParent = models.BigIntegerField()
    categoryImg = models.ImageField(upload_to='uploads/categories/')
    
    def __str__(self):
        return self.categoryName
    
    class Meta:
        db_table = 'category'