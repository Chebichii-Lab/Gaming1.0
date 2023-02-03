from django.urls import path
from . import views
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from django.conf import settings


urlpatterns=[
    path("", views.index, name="index"),
    path('upload/',views.game,name='add_game'),
    path('search/', views.search_game, name='search'),
    path(r'^game_details/(?P<id>\d+)', views.game_view, name='gamedetails'),
    path(r'^rate/(?P<game_id>\d+)', views.rate_game, name='rate'),
   
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)