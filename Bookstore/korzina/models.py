from django.db import models

# Create your models here.
class Books(models.Model):
	name = models.CharField(max_length=50)
	author = models.CharField(max_length=450)
	about = models.TextField()
	price = models.IntegerField()
	#imagess = models.ImageField()

	def __str__(self):
		return self.name