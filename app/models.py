from django.db import models

# Create your models here.
class Game(models.Model):
	matchname = models.CharField(max_length=225)
	creation_date = models.DateTimeField(auto_now_add=False, blank=True)

	def __str__(self):
		return self.matchname

class UserDetail(models.Model):
	username = models.CharField(max_length=120)
	rank = models.IntegerField(default=0)
	kills = models.IntegerField()
	score = models.IntegerField()
	game = models.ForeignKey('Game', related_name='games', on_delete=models.CASCADE,blank=True, null=True)
	games_list = models.ManyToManyField('Game', related_name='choices')

	def __str__(self):
		return self.username





