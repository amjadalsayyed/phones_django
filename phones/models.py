from django.db import models
from accounts.models import CustomUser
from django.urls import reverse
# Create your models here.
class Phones (models.Model):
    name = models.CharField(max_length=64)
    purchaser= models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    desc = models.TextField(default='blah blah blah')
    
    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('phones_list')