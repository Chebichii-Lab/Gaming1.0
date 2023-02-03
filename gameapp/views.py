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
			new_project = form.save(commit=False)
			new_project.user = current_user
			new_project.save()
			return redirect('index')
	else:
			form = GameForm()
	return render(request, 'game.html',{"form":form})