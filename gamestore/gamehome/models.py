from django.db import models

# Create your models here.
class Game(models.Model):
    game_id = models.IntegerField(primary_key="True")
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
    lmage_id = models.IntegerField(primary_key=True)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    def __str__(self):
        return self.lmage_id

class Game_type(models.Model):
    type_id = models.IntegerField(primary_key=True)
    type_name = models.CharField(max_length=50)
    def __str__(self):
        return self.type_id ,self.type_name
class User(models.Model):
    user_id = models.IntegerField(primary_key="True")

    # ------------------------------------------------------------------
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    def __str__(self):
        return self.username ,self.first_name

class User_games(models.Model):
    user_game_id = models.IntegerField(primary_key="True")
    user_id = models.ForeignKey("User", on_delete=models.CASCADE)
    game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
    # ------------------------------------------------------------------
    purchased_date = models.DateField()
    serial = models.IntegerField()