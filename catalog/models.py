from __future__ import unicode_literals


from django.db import models

# Create your models here.
class Books(models.Model):
	title=models.CharField(max_length=50)
	author=models.CharField(max_length=50)
	isbn=models.IntegerField()

	def __unicode__(self):
		return self.title
		
class Music(models.Model):
	title=models.CharField(max_length=50)
	singer=models.CharField(max_length=50)

	def __unicode__(self):
		return self.title

