from django.db import models


# Create your models here.
class Places(models.Model):
    place = models.CharField("Место", max_length=200)
    description = models.TextField("Комментарий")
    url = models.SlugField(max_length=160, default="places")
    latitude = models.FloatField("Широта", max_length=160, default=56.8389261)
    longitude = models.FloatField("Долгота", max_length=160, default=60.6057025)

    def __str__(self):
        return self.place

    class Meta:
        verbose_name = "Место"
        verbose_name_plural = "Места"

