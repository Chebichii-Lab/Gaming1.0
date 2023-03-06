
from django.shortcuts import render
from gameapp.forms import GameForm, RateForm,SignupForm, UserProfileForm
from gameapp.models import Game, Profile, Rate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, Http404,HttpResponseRedirect
from django.shortcuts import get_object_or_404, render,redirect
from django.urls import reverse
from django.shortcuts import redirect
from django.contrib.auth import authenticate, login




# Create your views here.

def index(request):
    games = Game.objects.all()
    profile = Profile.objects.all()
    rate = Rate.objects.all()
    return render(request,'index1.html', {'games':games,'profile':profile,'rate':rate})

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
def index(request):
    games = Game.objects.all()
    profile = Profile.objects.all()
    rate = Rate.objects.all()
    return render(request,'index.html', {'games':games,'profile':profile,'rate':rate})

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

	
@login_required(login_url='/accounts/login/')
def review_game(request,game_id):
    gam = Game.game_by_id(id=game_id)

    game = get_object_or_404(Game, pk=game_id)
    current_user = request.user
    if request.method == 'POST':
        form = RateForm(request.POST)
        if form.is_valid():

            content = form.cleaned_data['content']
            design = form.cleaned_data['design']
            usability = form.cleaned_data['usability']
            rate = Rate()
            # rate_avarage=(rate.usability +rate.design + rate.content)/3
            rate.game = game
            rate.user = current_user
            rate.usability = usability
            rate.design = design
            rate.content = content
            rate.average = (rate.usability +rate.design + rate.content)/3
            rate.save()
            # rate_avarage= (rate.average)/3
            # rate_avarage.save()
            return HttpResponseRedirect(reverse('gamedetails', args=(game.id,)))
    else:
        form = RateForm()
    return render(request, 'reviews.html', {"form":form,"user":current_user,"game":gam})     

@login_required(login_url='/accounts/login/')
def game_search(request): 
    if 'search_title' in request.GET and request.GET['search_title']:
        g_title = request.GET.get("search_title")
        searchResults = Game.search_game(g_title)
        message = f'g_title'
        results=searchResults
        message = message
        return render(request,'gamesearch.html', {'results':results,'message':message})
    else:
        message = "Your search did not match any game titles onboard."
    return render(request, 'gamesearch.html', {'message': message})    
      
