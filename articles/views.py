from django.shortcuts import render, redirect
from WebAppArticles.misc import htmlBuilder
from django.http import HttpResponse
from django.utils import timezone
from django.urls import reverse
from .models import Article
import json

# Create your views here.
def articleView(request, id):
    a = Article.objects.get(id = id)
    context = {
        "article": a,
        "content": htmlBuilder(False, a.content)
    }
    return render(request, 'article.html', context)

#http request require
#user auth require
def createView(request):
    article = Article.objects.create(
        title = "Sample Title",
        author = request.user,
        published = False,
        date = timezone.now(),
        content = [[{"type": "h1", "content" : "Sample"}]],
        likes = 0
    )
    article.save()
    return redirect('articles:edit', id = article.pk)

#http request require
#user auth require
def deleteView(request, id):
    ...

#user auth require
def editView(request, id):
    a = Article.objects.get(pk = id)
    
    if request.POST:
        packet = json.loads(request.POST['packet'])
        status = f"Last saved on {timezone.now().strftime("%H:%M")}"

        if a:
            a.title = packet["title"]
            a.content = packet["blocks"]
            a.published = packet["published"]
            if a.published:
                a.date = timezone.now()
            a.save()
            return HttpResponse(status)

        return HttpResponse("Error occured!")
    
    else:
        context = {
            "id": id,
            "article": a,
            "content": htmlBuilder(
                editor = True,
                blocks = a.content,
            ),
        }
        return render(request, 'editor.html', context = context)


def frontpageView(request):
    a = Article.objects.all()
    context = {
        "trending": a,
        "liked": a,
    }
    return render(request, 'frontpage.html', context)