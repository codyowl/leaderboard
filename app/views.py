from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Game, UserDetail
from .serializers import LeaderBoardSerializer
from django.shortcuts import get_object_or_404
from datetime import datetime
from datetime import timedelta
from django.http import HttpResponse
# Create your views here.
import json

def home(request):
	if request.method=="GET":
		return HttpResponse("Leader board webService is running!")


class LeaderBoardView(APIView):
	def get(self, request):
		time_threshold = None
		game_result = None
		matchname = request.GET.get('matchname', '')
		time = request.GET.get('time', '')
		if time=="last week":
			time_threshold = datetime.now() - timedelta(hours=168)
		elif time=="last day":
			time_threshold = datetime.now() - timedelta(hours=24)	
		elif time=="last month":
			time_threshold = datetime.now() - timedelta(hours=720)
		elif time=="alltime":
			time_threshold = None
		game = Game.objects.get(matchname=matchname)
		if time_threshold!=None:
			game_result = Game.objects.filter(creation_date=time_threshold, matchname=game)
			user = UserDetail.objects.filter(game__matchname=game_result).order_by('rank')
		else:
			user = UserDetail.objects.filter(game__matchname=game).order_by('rank')	

		serializer = LeaderBoardSerializer(user, many=True) #many for too many thigs in a list
		return Response({"stats":serializer.data})

class LeaderBoardViewBasedid(APIView):
	def get(self, request, pk):
		user = get_object_or_404(UserDetail.objects.all(), pk=pk)
		user_rank = user.rank
		matchname = request.GET.get('matchname', '')

		game = Game.objects.get(matchname=matchname)
		user_filter = UserDetail.objects.filter(game=game).order_by('rank')
		# to get user adjacent rank list out upto 5
		adjacent_rank_user = [u for u in user_filter if u.rank>user_rank]
		# upto adjacent ranks 5
		adjance_rank = adjacent_rank_user[4:]
		serializer = LeaderBoardSerializer(adjance_rank, many=True) #many for too many thigs in a list
		return Response({"stats":serializer.data})

class PlayerStatsView(APIView):
	def get(self, request, pk):
		user = get_object_or_404(UserDetail.objects.all(), pk=pk)
		games_list = [game for game in user.games_list]
		total_game_details = []
		for g in games_list:
			total_game_details.append(UserDetail.objects.filter(game=game))
		serializer = LeaderBoardSerializer(user, many=True)
		return Response({"Playerstats":serializer.data})			

class PlayerStatsIndivView(APIView):
	def get(self, request, pk):
		time_threshold = None
		matchname = request.GET.get('matchname', '')
		time = request.GET.get('time', '')
		if time=="last week":
			time_threshold = datetime.now() - timedelta(hours=168)
		elif time=="last day":
			time_threshold = datetime.now() - timedelta(hours=24)	
		elif time=="last month":
			time_threshold = datetime.now() - timedelta(hours=720)
		elif time=="alltime":
			time_threshold = None
		game = Game.objects.get(matchname=matchname)
		if not time_threshold:
			game_result = Game.objects.filter(creation_date=time_threshold, matchname=game)
		user_filter = UserDetail.objects.filter(game=game_result).order_by('rank')
		adjacent_rank_user = [u for u in user_filter if u.rank>user_rank]
		serializer = LeaderBoardSerializer(user, many=True)
		return Response({"Playerstats":serializer.data})			
