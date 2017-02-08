from django.db import models

# Create your models here.

class LibBaseModel(models.Model):
    title = models.CharField(max_length=50)
    artist = models.CharField(max_length=50)
    date = models.DateField()
    date_added = models.DateField(auto_now_add=True)
    length = models.DurationField()

    class Meta:
        abstract = True

class Track(LibBaseModel):
    album_name = models.CharField(max_length=50)
    album_id = models.ForeignKey('Album', on_delete=models.DO_NOTHING)

    #audiofield goes here

    def __str__(self):
        return self.title

class Album(LibBaseModel):

    def __str__(self):
        return self.title
