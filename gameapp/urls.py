from django.urls import path
from django.urls import re_path as url
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    path("", views.index, name="index"),
    url('register/',views.register, name='registration'),
    url('login/',auth_views.LoginView.as_view(), name='login'),
    url('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    url('profile/',views.profile, name='profile'), 
    url('game/',views.game,name='gameupload'),
    url('gamedetails/(?P<id>\d+)',views.game_view,name='gamedetails'),
    url('review/(?P<game_id>\d+)', views.review_game, name='review'), 
    url('search/', views.game_search,name='search'),
      
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)