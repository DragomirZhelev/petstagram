from django.db import models
from django.conf import settings

from petstagram.photos.models import Photo


# Create your models here.
class Comment(models.Model):
    text = models.TextField(max_length=300)
    date_time_of_publication = models.DateTimeField(auto_now_add=True)
    to_photo = models.ForeignKey(Photo, related_name='photo_comments', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='comments')

    class Meta:
        ordering = ('-date_time_of_publication',)


class Like(models.Model):
    to_photo = models.ForeignKey(Photo, related_name='likes', on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='likes')

