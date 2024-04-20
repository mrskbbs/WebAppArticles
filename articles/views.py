from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST, require_GET
from django.shortcuts import render, redirect
from WebAppArticles.misc import htmlBuilder, getLiked
from django.http import HttpResponse
from django.utils import timezone
from .models import Article
from WebAppArticles.misc import user_isauthor
import json


def articleView(request, pk):
    article = Article.objects.get(id = pk)
    context = {
        "article": article,
        "content": htmlBuilder(False, article.content),
        "liked": getLiked(request.user.id),
    }
    return render(request, 'article.html', context)


@require_GET
@login_required(login_url = "users:signup")
def createView(request):
    article = Article.objects.create(
        title = "Sample Title",
        author = request.user,
        published = False,
        date = timezone.now(),
        content = [[{"type": "h1", "content" : "Sample"}]],
    )
    article.save()
    return redirect('articles:edit', pk = article.pk)

@require_POST
@user_isauthor(redirect_url = "frontpage")
@login_required(login_url = "users:signup")
def deleteView(request, pk):
    article = Article.objects.get(id = pk)
    author_id = article.author.id
    article.delete()

    origin = request.META["HTTP_REFERER"]
    return redirect(origin, id = author_id)

@require_POST
@login_required(login_url = "users:signup")
def likeView(request, pk):
    article = Article.objects.get(id = pk)
    origin = request.META["HTTP_REFERER"]
    if article.users_liked.contains(request.user):
        article.users_liked.remove(request.user)
    else:
        article.users_liked.add(request.user)

    return redirect(origin, pk = pk)


@user_isauthor(redirect_url = "frontpage")
@login_required(login_url = "users:signup")
def editView(request, pk):
    a = Article.objects.get(id = pk)
    
    if request.method == "POST":
        packet = json.loads(request.body.decode("utf-8"))

        if a:
            a.title = packet["title"]
            a.content = packet["blocks"]
            a.published = packet["published"]
            if a.published:
                a.date = timezone.now()
            a.save()
        
        return HttpResponse("Error 404")
    
    
    else:
        context = {
            "article": a,
            "content": htmlBuilder(
                editor = True,
                blocks = a.content,
            ),
        }
        return render(request, 'editor.html', context = context)


def frontpageView(request):
    article = Article.objects.all()
    context = {
        "trending": article,
        "mostliked": article,
        "liked": getLiked(request.user.id),
    }
    return render(request, 'frontpage.html', context)