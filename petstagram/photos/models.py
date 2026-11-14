from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_size
from django.conf import settings


# Create your models here.
class Photo(models.Model):
    photo = models.ImageField( upload_to='images', validators=[validate_file_size])
    description = models.TextField(max_length=300, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30, blank=True, null=True)
    tagged_pets = models.ManyToManyField(Pet, related_name='tagged_pets', blank=True)
    date_of_publication = models.DateField(auto_now=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='photos')



    def __str__(self):
        return self.description