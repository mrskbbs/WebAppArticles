from django.shortcuts import redirect, render, HttpResponse
from articles.models import Article
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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
    if hasattr(request, "POST") and request.POST != {}:
        user = authenticate(
            username = request.POST["username"],
            password = request.POST["password"],
        )
        if user:
            print(user)
            login(request, user)
            return redirect(reverse("frontpage"))

        return HttpResponse("There is not such user")

    return render(request, 'login.html')

def logoutView(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(reverse("frontpage"))

# If not signed in
def signupView(request):
    
    if hasattr(request, "POST") and request.POST != {}:
        user = User.objects.create_user(
            username = request.POST["username"],
            password = request.POST["password"],
        )
        user.save()

        login(request, user)

        return redirect(reverse("frontpage"))

    return render(request, 'signup.html')

