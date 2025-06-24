from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name
class Stock(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30, unique=True)
    quantity = models.IntegerField(default=1)
    is_deleted = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)  # <-- AGREGA ESTA LÍNEA


    def __str__(self):
	    return self.name