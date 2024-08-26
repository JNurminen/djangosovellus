from django.db import models

# Luodaan Band ja Album -mallit

class Band(models.Model):
    name = models.CharField(max_length=50, default='Unknown')
    country = models.CharField(max_length=50, default='Unknown')
    genre = models.CharField(max_length=50, default='Unknown')
    year = models.IntegerField()
    def __str__(self):
        return f"{self.name} from {self.country}"
    
class Album(models.Model):
    name = models.CharField(max_length=50, default='Unknown')
    band = models.ForeignKey(Band, on_delete=models.CASCADE)
    year = models.IntegerField()
    def __str__(self):
        return f"{self.name} by {self.band.name}"