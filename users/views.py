from django.shortcuts import redirect, render, HttpResponse
from articles.models import Article
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from WebAppArticles.misc import logout_required, getLiked
from django.urls import reverse

def profileView(request, id):
    profile = User.objects.get(id = id)
    if profile:
        
        user_articles = Article.objects.filter(author = profile)
        total_likes = 0

        for article in user_articles:
            total_likes += article.users_liked.count()
        
        context = {
            "profile": profile,
            "profile_likes": total_likes,
            "liked": getLiked(request.user.id),
            "articles": Article.objects.all().filter(author = profile), 
        }
        
        return render(request, "profile.html", context)
    return HttpResponse("There isn't such user")

@logout_required(redirect_url = "frontpage")
def loginView(request):
    form = AuthenticationForm(None, data = request.POST)
    context = {
        "form": form,
    }

    if hasattr(request, "POST") and request.POST != {}:
        if form.is_valid():        
            login(request, form.get_user())
            return redirect(reverse("frontpage"))

    return render(request, 'login.html', context)

@login_required(login_url = "users:signup")
def logoutView(request):
    logout(request)
    return redirect(reverse("frontpage"))

@logout_required(redirect_url = "frontpage")
def signupView(request):
    form = UserCreationForm(request.POST or None)
    context = {
        "form": form,
    }
    if hasattr(request, "POST") and request.POST != {}:
        if form.is_valid():
            user = form.save()
            user.is_active = True
            user.save()
            login(request, user)

            return redirect(reverse("frontpage"))

    return render(request, 'signup.html', context)

