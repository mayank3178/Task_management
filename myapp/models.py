from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.

class Task(models.Model):
	id=models.IntegerField(primary_key=True)
	taskname=models.CharField(max_length=100,null=False,blank=False)
	taskcompletiondate=models.DateTimeField(default=timezone.now,null=False)
	taskdescription=models.TextField(null=False)

	def __str__(self):
		return self.taskname

		
	
		