from django.db import models

# Create your models here.



class Songs(models.Model):
    artist = models.CharField(max_length=20) 
    title = models.CharField(max_length=20)
    uploadFile = models.FileField(blank=True,null=True)
    details =models.CharField(max_length=120,blank=True,null=True)
    def __str__(self):
        return "id :{},artist :{},title :{},uploadFile :{}" .format(self.id,self.artist,self.title,self.uploadFile)