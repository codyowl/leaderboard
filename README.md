# api routes
 - baseurl/api/leaderboard/?matchname="MATCHNAME"&time="TIMEOPTION"
 - baseurl/api/leaderboard/<USER_ID>/?matchname="MATCHNAME"
 - baseurl/api/playerstats/?matchname="MATCHNAME"&time="TIMEOPTION"
 - baseurl/api/playerstats/<USER_ID>/?matchname="MATCHNAME"
 - ## TIMEOPTION:
      -  all time        -> will give result based on all time
      -  last week       -> will give result based on games that were created in last week
      -  last day        -> will give result based on games that were created in last day
      -  last month      -> will give result based on games that were created in last month
   

# Running the project:
## Installing pre requisites:
  
    In the file name "requirements.txt" project's pre requisites will be listed out
    go inside project root folder
    install using the following command:
    pip3 install -r requirements.txt
  


## settings.py tweaks : comment the following heroku's database settings for running it on local:
   
     DATABASES = {
         'default': dj_database_url.config(
             default=config('DATABASE_URL')
         )
     }
     
## migrate the db using the management command:

   
    python manage.py makemigraitons
    python manage.py migrate
   
## running the server:
   
    python manage.py runserver
   
## Database models:

   - Creating Users:
      
         from django.app.models import UserDetail
         user = UserDetail.objects.create(username="USERNAME", rank="RANK", kills="KILLS", score="SCORE", game="GAME OBJECT", games_list = "GAMES LIST OBJECT"

   - Creating Games:
         
          from app.models import Game
          game = Game.objects.create(matchname="MATCHNAME") 
          
          
# leaderboard

![leaderboard_alltime](https://user-images.githubusercontent.com/9798362/65917150-5ccd6200-e3f4-11e9-9d62-c999c2ffc446.png)


## adjacent ranks

![adjacent_ranklist](https://user-images.githubusercontent.com/9798362/65917173-65be3380-e3f4-11e9-8833-925de745a753.png)
