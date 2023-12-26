from django.db import models

# Create your models here.
class DEPT(models.Model):
    deptno=models.IntegerField(primary_key=True)

