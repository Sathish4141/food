from django.db import models

# Create your models here.


class Items(models.Model):
    category = models.CharField(max_length=40)
    sub_category = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    rate = models.FloatField()

    def __str__(self) -> str:
        return self.name

        
