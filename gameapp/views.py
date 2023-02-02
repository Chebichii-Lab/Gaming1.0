from django.shortcuts import render
from gameapp.models import Game, Profile, Rate


# Create your views here.
def index(request):
    game = Game.objects.all()
    profile = Profile.objects.all()
    rate = Rate.objects.all()
    return render(request,'index.html', {'game':game,'profile':profile,'rate':rate})
