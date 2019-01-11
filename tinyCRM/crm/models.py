from django.db import models
from django.contrib.auth.models import User

class Case(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)
    date_updated = models.DateField(auto_now=True)

    def __str__(self):
        return self.last_name + ' ' + self.first_name

class Interaction(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    case = models.ForeignKey(Case, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateField(auto_now_add=True)

    @property
    def __str__(self):
        return self.title + ' on ' + self.date_created