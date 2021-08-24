from django.db import models

# Create your models here.
class Category(models.Model):
    category = models.CharField(max_length= 80)

    def __str__(self):
        return self.category


class Book(models.Model):
    title = models.CharField(max_length=250)
    isbn = models.CharField(max_length=13)
    author = models.CharField(max_length=80)
    pub_year = models.DateField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

