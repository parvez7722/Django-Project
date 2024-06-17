from django.db import models
from django.contrib.auth.models import User

class Categorie(models.Model):
    categorie_name = models.CharField(max_length=100)

    def __str__(self):
        return self.categorie_name

class Product(models.Model):
    product_categorie = models.ForeignKey(Categorie,related_name='Products',on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    product_description = models.CharField(blank=True,null=True,max_length=500)
    product_price = models.FloatField(null=False,blank=False,default=0)
    product_user = models.ForeignKey(User,related_name='Product',on_delete=models.CASCADE)

    def __str__(self):
        return self.product_name
