from django.db import models
from django.contrib.auth.models import User
# Create your models here.



class Savatcha(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    telefon = models.CharField(max_length=20, null=False)
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)



class Buyurtma(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=150)
    telefon_raqam = models.CharField(max_length=20, null=False)
    jami_narx = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)



