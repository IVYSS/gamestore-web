from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.IntegerField(primary_key=True,default=0)
    # ------------------------------------------------------------------
    name = models.CharField(max_length=50)
    description = models.TextField()
    game_type_id = models.IntegerField()
    developer = models.TextField()
    rating = models.IntegerField()
    release_date = models.DateField()
    price = models.IntegerField()

    def __str__(self):
        return self.name

class Lmage(models.Model):
    lmage_id = models.IntegerField(primary_key=True,default=0)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)

class Game_type(models.Model):
    type_id = models.IntegerField(primary_key=True, default=0)
    type_name = models.CharField(max_length=50)
    def __str__(self):
        return self.type_name
class User(models.Model):
    user_id = models.IntegerField(primary_key=True,default=0)

    # ------------------------------------------------------------------
    username = models.CharField(max_length=50, null=True)
    password = models.CharField(max_length=50, null=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    email = models.EmailField(max_length=254, null=True)
    def __str__(self):
        return self.username ,self.first_name

class User_games(models.Model):
    user_game_id = models.IntegerField(primary_key=True,default=0)
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    # ------------------------------------------------------------------
    purchased_date = models.DateField()
    serial = models.IntegerField()