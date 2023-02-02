from django.db import models
from django.contrib.auth.models import User
from PIL import Image

# Create your models here.
class Profile(models.Model):
    profile_picture = models.ImageField('image')
    profile_bio = models.TextField()
    profile_contact = models.CharField(max_length=60,blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="profile",primary_key=True)

    def __str__(self):
        return self.user.username

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

class Game(models.Model):
    game_title = models.CharField(max_length=60,blank=True)
    game_image = models.ImageField('image')
    game_description = models.TextField()
    game_link = models.URLField(blank=True)
    user = models.ForeignKey(User, null=True,on_delete=models.CASCADE)
    profile = models.ForeignKey(Profile,null=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.game_title

    def save_game(self):
        self.save()

    def delete_game(self):
        self.delete()

    @classmethod
    def game_by_id(cls,id):
        game = Game.objects.filter(id =id)
        return game

    @classmethod
    def search_by_game_title(cls,search_term):
        games = cls.objects.filter(_title__icontains=search_term)
        return games

class Rate(models.Model):
    RATE_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
        (6, '6'),
        (7, '7'),
        (8, '8'),
        (9, '9'),
        (10, '10'),
    )
    design = models.IntegerField(choices=RATE_CHOICES,default=0,blank=False)
    usability = models.IntegerField(choices=RATE_CHOICES,default=0,blank=False)
    content = models.IntegerField(choices=RATE_CHOICES,default=0,blank=False)
    average =  models.DecimalField(default=1,blank=False,decimal_places=2,max_digits=100)
    game = models.ForeignKey(Game,null=True,on_delete=models.CASCADE)
    user = models.ForeignKey(User,null=True,blank=True,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_rate(self):
        self.save()

    def delete_rate(self):
        self.delete()
