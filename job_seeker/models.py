from django.db import models
from django.contrib.auth.models import User
from employer.models import Job

# Create your models here.
class Application(models.Model):
    job = models.ForeignKey(to=Job, related_name='job', on_delete=models.CASCADE)
    user = models.ForeignKey(to=User, related_name='user', on_delete=models.CASCADE)
    resume = models.FileField(upload_to='resume/')
    application_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user} apply for {self.job}"
    
    
    
    