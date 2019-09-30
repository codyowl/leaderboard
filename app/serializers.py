from rest_framework import serializers
from .models import UserDetail


class LeaderBoardSerializer(serializers.Serializer):
	username = serializers.CharField(max_length=200)
	rank = serializers.IntegerField()
	kills = serializers.IntegerField()
	score = serializers.IntegerField()
	# game = serializers.IntegerField()
