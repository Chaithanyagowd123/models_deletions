from django.db import models

# Create your models here.
class Country(models.Model):
    Cname=models.CharField(max_length=100,primary_key=True)


class Capital(models.Model):
    cname=models.ForeignKey(Country,on_delete=models.CASCADE)
    capitalname=models.CharField(max_length=100)
    url=models.CharField(max_length=100)
    