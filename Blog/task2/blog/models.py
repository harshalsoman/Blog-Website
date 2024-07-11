from django.db import models

# Create your models here.
class blogform(models.Model):
    Title= models.CharField(max_length=255)
    Date= models.DateField()
    Content=models.TextField()
    Image= models.ImageField(null=True,blank=True,upload_to= "my_images")

#class Image(models.Model):
    #pic=models.ImageField(upload_to='myimages')

