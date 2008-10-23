from django.db import models
from datetime import datetime
from django.contrib.auth.models import User

class Channel(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    url = models.CharField(max_length=200)
    added_date = models.DateTimeField(default=datetime.now)
    creator = models.ForeignKey(User)
    votes =  models.IntegerField()
    
    def __unicode__(self):
        return "%s: %s er lagt til" % (self.name, self.url)
        
        
    
    
    
    
    
    
