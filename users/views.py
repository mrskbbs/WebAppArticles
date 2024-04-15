from django.shortcuts import redirect, render, HttpResponse
from articles.models import Article
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from WebAppArticles.misc import logout_required
from django.urls import reverse

def profileView(request, pk):
    profile = User.objects.get(pk = pk)
    if profile:
        
        user_articles = Article.objects.filter(author = profile)
        total_likes = 0

        for article in user_articles:
            total_likes += article.likes 
        
        context = {
            "profile": profile,
            "likes": total_likes,
        }
        
        return render(request, "profile.html", context)
    return HttpResponse("There isn't such user")

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

# Write the decorators
# @logout_required(redirect_url = "frontpage")
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

