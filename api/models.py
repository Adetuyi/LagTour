from django.db import models

# Create your models here.


class Location(models.Model):
    name = models.CharField(max_length=200)
    location_image = models.ImageField(
        null=True, blank=True, upload_to="images/")
    coordinate_x: models.IntegerField(null=True, blank=True)
    coordinate_y: models.IntegerField(null=True, blank=True)
    is_popular = models.BooleanField(default=False, blank=True, null=True)
    wikipedia_link = models.URLField(default=False, blank=True, null=True)
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
