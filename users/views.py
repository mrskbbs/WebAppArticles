from django.shortcuts import render

# Create your views here.
def profile(request):
    return render(request, "profile.html")

def login(request):
    return render(request, 'article.html')

def signup(request):
    return render(request, 'article.html')

