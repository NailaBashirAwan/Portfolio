from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill
# Create your models here.
class skills(models.Model):
    skill_name=models.CharField(max_length=100)
    skill_percentage=models.IntegerField()

    def __str__(self):
        return self.skill_name
    
class Services(models.Model):
    service_name=models.CharField(max_length=100)
    service_description=models.TextField()
    service_icon=models.CharField(max_length=100)
    # service_icon=models.ImageField(upload_to='services_icons/')

    def __str__(self):
        return self.service_name
    
class PortfolioItem(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=200, blank=True, null=True)
    project_date = models.DateField()
    project_url = models.URLField(blank=True, null=True)
    description = models.TextField()
    image = models.ImageField(upload_to='projects/', blank=True, null=True)  # store images in MEDIA folder
    thumbnail = ImageSpecField(source='image',
                                processors=[ResizeToFill(500, 500)],
                                format='JPEG',
                                options={'quality': 100})
    def __str__(self): 
        return self.title