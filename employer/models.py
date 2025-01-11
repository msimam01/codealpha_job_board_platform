from django.db import models

# Create your models here.
class Job(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    posted_date = models.DateField(auto_now_add=True)
    deadline = models.DateField()
    
    def __str__(self):
        return f"{self.title} {self.description}"
    

