from django.db import models

# Create your models here.

class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField (max_length=50)
    phone = models.CharField(max_length=10)
    email=models.EmailField()
    password = models.CharField(max_length=100)
    
    def __str__(self):
        return self.first_name
    
    class Meta:
        db_table = 'customer'
