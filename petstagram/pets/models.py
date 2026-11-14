from django.db import models
from django.template.defaultfilters import slugify
from django.conf import settings


# Create your models here.
class Pet(models.Model):
    name = models.CharField(max_length=30)
    pet_photo = models.URLField(blank=True)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, null=False, blank=True, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pets')

    def save(self, *args, **kwargs):
        if not self.pk:
            super().save(*args, **kwargs)

        self.slug = slugify(f'{self.name}-{self.pk}')
        super().save(*args, **kwargs)

    def __str__(self):
        return self.name