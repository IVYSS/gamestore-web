from django.contrib import admin
from gamehome.models import Game,Lmage,Game_type,User,User_games

# Register your models here.
class GameInline(admin.StackedInline):
    model = Lmage
    extra = 3
class GamePer(admin.ModelAdmin):
    list_per_page = 5
    fieldsets = [
        ('ID', {'fields': ['game_id','game_type_id']}),
        ('Information', {'fields': ['name','description','developer']}),
        ('Price', {'fields': ['rating','price']}),
        ('Date', {'fields': ['release_date']}),
        
    ]
    inlines = [GameInline]
admin.site.register(Game, GamePer)

class PerLmage(admin.ModelAdmin):
    list_per_page = 5
admin.site.register(Lmage, PerLmage)
# 


class PerGame_type(admin.ModelAdmin):
    list_per_page = 5
     
    
admin.site.register(Game_type, PerGame_type)


class PerUser(admin.ModelAdmin):
    list_per_page = 5
admin.site.register(User)

class PerUser_games(admin.ModelAdmin):
    list_per_page = 5
admin.site.register(User_games, PerUser_games)






