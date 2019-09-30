from django.urls import path, re_path
from .views import LeaderBoardView, LeaderBoardViewBasedid, PlayerStatsView, PlayerStatsIndivView

app_name = "articles"

urlpatterns = [
	# path('articles/', ArticleView.as_view()),
	# path('alluser/', AllUser.as_view()),
	# path('leaderboard/<string:matchname>/<string:time>', LeaderBoardView.as_view())
	# re_path(r'^leaderboard/', LeaderBoardView.as_view())
	path('leaderboard/', LeaderBoardView.as_view()),
	path('leaderboard/<int:pk>/', LeaderBoardViewBasedid.as_view()),
	path('playerstats/', PlayerStatsView.as_view()),
	path('playerstats/<int:pk>/', PlayerStatsIndivView.as_view()),
]