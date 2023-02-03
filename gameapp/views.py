from django.shortcuts import render
from gameapp.forms import GameForm
from gameapp.models import Game, Profile, Rate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect



# Create your views here.
def index(request):
    game = Game.objects.all()
    profile = Profile.objects.all()
    rate = Rate.objects.all()
    return render(request,'index.html', {'game':game,'profile':profile,'rate':rate})


@login_required(login_url='/accounts/login')
def game(request):
	current_user = request.user
	if request.method == 'POST':
		form = GameForm(request.POST,request.FILES)
		if form.is_valid():
			new_game = form.save(commit=False)
			new_game.user = current_user
			new_game.save()
			return redirect('index')
	else:
			form = GameForm()
	return render(request, 'game.html',{"form":form})

@login_required(login_url='/accounts/login')
def game_view(request,id):
    game = Game.objects.get(id = id)
    rates = Rate.objects.all()
    return render(request, 'game_view.html',{"rates":rates,"game":game})