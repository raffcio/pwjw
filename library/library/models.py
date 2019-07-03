from django.db import models


class Book(models.Model):
	pId=models.IntegerField()
	name=models.TextField()
	desc=models.TextField()
	awLink=models.URLField()
	awThumb=models.URLField()
	awImage=models.URLField()
	ilosc=models.IntegerField()