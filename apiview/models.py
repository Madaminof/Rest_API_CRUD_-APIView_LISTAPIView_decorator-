from django.db import models


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'category'

    def __str__(self):
        return f"{self.name} {self.pk}"


class MusicKlip(models.Model):
    objects = None
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    audio = models.FileField(upload_to='audio/', null=True, blank=True)
    docPDF = models.FileField(upload_to='doc/', null=True)

    class Meta:
        db_table = 'music_klip'

    def __str__(self):
        return f"{self.name}  {self.pk} "
