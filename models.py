from django.db import models
from django.contrib.auth.models import User
from datetime import datetime, date

# Create your models here.
class Dashboards(models.Model):
    
    
    
    SiteName = models.CharField(max_length = 10)
    # DateCreated = models.DateField(auto_now_add=False, auto_now=False)
    def __str__(self):
        return self.SiteName


