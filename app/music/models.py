from django.db import models
class Album(models.Model):
    artist = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    genere = models.CharField(max_length=100)
    logo = models.CharField(max_length=1000)
    def __str__(self):
        return self.artist +"-"+self.title
class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    is_favorite=models.BooleanField(default=False)
    def __str__(self):
        return self.title
