from django.shortcuts import render
from gameapp.forms import GameForm,SignupForm, UserProfileForm
from gameapp.models import Game, Profile, Rate
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    games = Game.objects.all()
    profile = Profile.objects.all()
    rate = Rate.objects.all()
    return render(request,'index.html', {'games':games,'profile':profile,'rate':rate})

def register(request):
    if request.method=="POST":
        form=SignupForm(request.POST) 
        if form.is_valid():
           form.save()
           username = form.cleaned_data.get('username')
           user_password = form.cleaned_data.get('password1')
           user = authenticate(username=username, password=user_password)
           login(request, user)
        return redirect('login')
    else:
        form= SignupForm()
    return render(request, 'registration/registration_form.html', {"form":form})  


@login_required(login_url='/accounts/login/') 
def profile(request):
    if request.method == 'POST':
        user_profile_form = UserProfileForm(request.POST, request.FILES, instance=request.user)
        if  user_profile_form.is_valid():
            user_profile_form.save()
            return redirect('home')
    else:
        user_profile_form = UserProfileForm(instance=request.user)
    return render(request, 'profile.html',{"user_profile_form": user_profile_form})  

@login_required(login_url='/accounts/login/') 
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

@login_required(login_url='/accounts/login/') 
def game_view(request,id):
    game = Game.objects.get(id = id)
    rates = Rate.objects.all()
    return render(request, 'game_view.html',{"rates":rates,"game":game})
	