from django.shortcuts import render
from django.http import HttpResponse 

from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "register.html", {"form": form})

def user_login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("profile")
    return render(request, "login.html")

def user_logout(request):
    logout(request)
    return redirect("login")

def profile(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    profile, created = RoommateProfile.objects.get_or_create(user=request.user)
    if request.method == "POST":
        profile.bio = request.POST.get('bio', '')
        profile.interests = request.POST.get('interests', '')
        profile.location = request.POST.get('location', '')
        profile.budget = request.POST.get('budget', 0)
        profile.save()
    return render(request, "profile.html", {"profile": profile})

def find_matches(request):
    if not request.user.is_authenticated:
        return redirect("login")
    
    try:
        user_profile = RoommateProfile.objects.get(user=request.user)
    except RoommateProfile.DoesNotExist:
        return redirect("profile")
    
    potential_matches = RoommateProfile.objects.exclude(user=request.user)
    matches = []
    for profile in potential_matches:
        score = similarity_score(user_profile, profile)
        matches.append({"profile": profile, "score": score})
    matches = sorted(matches, key=lambda x: x["score"], reverse=True)
    return render(request, "matches.html", {"matches": matches})

def similarity_score(profile1, profile2):
    interests1 = set(profile1.interests.split(",")) if profile1.interests else set()
    interests2 = set(profile2.interests.split(",")) if profile2.interests else set()
    common_interests = interests1 & interests2
    return len(common_interests) / max(len(interests1), 1)