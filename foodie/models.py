from django.db import models

# Create your models here.
class Restaurant(models.Model):
	rest_ID = models.IntegerField()
	name = models.CharField(max_length=50)
	lat = models.CharField(max_length=50)
	lon = models.CharField(max_length=50)
	url = models.CharField(max_length=100)
	img_url = models.CharField(max_length=150)
	rating = models.DecimalField(max_digits=3,decimal_places=2)

	def __unicode__(self):
		return self.name