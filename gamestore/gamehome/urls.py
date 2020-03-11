from django.urls import path
from gamehome import views
urlpatterns = [
    path('', views.showgame, name="showgame"),
    # path('seemore/', views.show_all_detail, name="show_all_detail"),
    # path('information/', views.show_information, name="show_information"),
    path('seemore/<int:seemore>',views.seemore, name="seemore"),
    path('detail/<int:detail>', views.detail, name="detail"),
   
]
