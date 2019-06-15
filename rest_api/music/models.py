from django.db import models

# Create your models here.



class Songs(models.Model):
    artist = models.CharField(max_length=20) 
    title = models.CharField(max_length=20)
    uploadFile = models.FileField(blank=True,null=True)

    def __str__(self):
        return "id is = {} - {} - {} - {}" .format(self.id,self.artist,self.title,self.uploadFile)