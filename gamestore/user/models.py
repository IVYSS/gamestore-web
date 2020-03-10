from django.db import models
# Create your models here.
# class User(models.Model):
#     user_id = models.IntegerField(primary_key="True")

#     # ------------------------------------------------------------------
#     username = models.CharField(max_length=50)
#     password = models.CharField(max_length=50)
#     first_name = models.CharField(max_length=50)
#     last_name = models.CharField(max_length=50)
#     email = models.EmailField(max_length=254)

# class User_games(models.Model):
#     user_game_id = models.IntegerField(primary_key="True")
#     user_id = models.ForeignKey("User", on_delete=models.CASCADE)
#     game_id = models.ForeignKey("Game", on_delete=models.CASCADE)
#     # ------------------------------------------------------------------
#     purchased_date = models.DateField()
#     serial = models.IntegerField()