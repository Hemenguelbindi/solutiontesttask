from django.db import models



class Items(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    price = models.IntegerField()

    def __str__(self):
        return self.name