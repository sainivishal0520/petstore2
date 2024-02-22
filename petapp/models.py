from django.db import models


class BreedManager(models.Manager):
    def get_pet_by_breed(self, breed):
        return self.filter(breed=breed)

# Create your models here.
class pet(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length = 50)
    breed = models.CharField(max_length = 100)
    
    objects = BreedManager()
    
    def __str__(self):
        return self.name
