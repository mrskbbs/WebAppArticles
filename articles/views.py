from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Article
from WebAppArticles.misc import htmlBuilder
import json

# Create your views here.
def article(request, id):
    return render(request, 'article.html')

#http request require
#user auth require
def create(request, id):
    ...
    
#http request require
#user auth require
def delete(request, id):
    ...

#user auth require
def edit(request, id):
    a = Article.objects.get(pk = id)
    
    if request.POST:
        packet = json.loads(request.POST['packet'])
        status = f"Last saved on {timezone.now().strftime("%H:%M")}"

        if a:
            a.title = packet["title"]
            a.content = packet["blocks"]
            a.published = packet["published"]
            return HttpResponse(status)

        return HttpResponse("Error occured!")
    
    else:
        context = {
            "id": id,
            "content": htmlBuilder(
                editor = True,
                blocks = a.content,
            ),
        }
        return render(request, 'editor.html', context = context)


def frontpage(request):
    return render(request, 'frontpage.html')