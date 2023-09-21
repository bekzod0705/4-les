from django.db import models
from datetime import datetime
# Create your models here.

class CarModel(models.Model):
    name=models.CharField(max_length=80,default='')
    price=models.PositiveIntegerField()
    isEloctrocar=models.BooleanField(default=False)
    created=models.DateTimeField(default=datetime.now)
    def __str__(self) -> str:
        return self.name