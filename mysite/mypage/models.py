from django.db import models

# Create your models here.

class CricketerNames(models.Model):
	playerName = models.CharField(max_length=200)
	playerRole = models.CharField(max_length=200)

	def __str__(self):
		return self.playerName
		return self.playerRole	