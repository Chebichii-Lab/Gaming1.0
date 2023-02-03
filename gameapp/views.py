from django.shortcuts import render, redirect, get_object_or_404
from gameapp.forms import GameForm, RateForm
from gameapp.models import Game, Profile, Rate
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect
from django.urls import reverse




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

@login_required(login_url='/accounts/login/')
def rate_game(request,game_id):
    games = Game.game_by_id(id=game_id)
    game = get_object_or_404(Game, pk=game_id)
    current_user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():

            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            content = form.cleaned_data['content']
            rate = Rate()
            rate.game = game
            rate.user = current_user
            rate.design = design
            rate.usability = usability
            rate.content = content
            rate.average = (rate.design + rate.usability + rate.content)/3
            rate.save()
            return HttpResponseRedirect(reverse('ratedetails', args=(rate.id,)))
    else:
        form = RateForm()
    return render(request, 'rates.html', {"user":current_user,"game":games,"form":form})