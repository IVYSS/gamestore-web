from django.urls import path
from user import views
urlpatterns = [
    path('login/', views.my_login, name="login"),
    path('logout/', views.user_logout, name="logout"),
    # path('information/', views.register, name="information"),
    path('register/', views.register, name="register"),
]
