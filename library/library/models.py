import random
from django.db import models
from xml.etree import ElementTree 


class Book(models.Model):
	pId=models.IntegerField()
	name=models.TextField()
	desc=models.TextField()
	awLink=models.URLField()
	awThumb=models.URLField()
	awImage=models.URLField()
	ilosc=models.IntegerField()
	
def DBImport():
	xmltree = ElementTree.parse('library\\inbook.xml')
	produkty = xmltree.getroot()
	i=0
	if produkty is not None:
		for prod in produkty.findall('prod'):		
			i=i+1
			print(i)
			b = Book(pId=prod.find("pId").text ,	name=prod.find("name").text ,	desc=prod.find("desc").text or "",	awLink=prod.find("awLink").text ,	awThumb=prod.find("awThumb").text ,	awImage=prod.find("awImage").text ,	ilosc=random.randint(1,10)) 
			b.save()