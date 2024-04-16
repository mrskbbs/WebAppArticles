from articles.models import Article
from django.shortcuts import resolve_url, redirect
from functools import wraps
import re 

def htmlSanitize(s: str) -> str:
    HTMLREG: str = "<[^<>]*>"
    
    m: re.Match = re.search(HTMLREG, s)
    while m != None:
        start, end = m.span()
        s = f"{s[:start]}&lt{s[start+1:end-1]}&gt{s[end:]}"
        m = re.search(HTMLREG, s)
    
    return s

def htmlBuilder(editor: bool, blocks: list[list[str]]) -> str:
    html: str = ""

    if editor:
        TEMPLATES: dict[str, str] = {
            "h1": "<textarea class = 'h1' rows = '1'>{}</textarea>",
            "p": "<textarea class = 'p' rows = '10'>{}</textarea>",
        }
    else:
        TEMPLATES: dict[str, str] = {
            "h1": "<h1>{}</h1>",
            "p": "<p>{}</p>",
        }
    
    for block in blocks:
        node: str = ""
        
        for element in block:
            if not editor:
                element["content"] = htmlSanitize(element["content"])

            node += TEMPLATES[element["type"]].format(element["content"])
        
        html += f"<div class = 'block'>{node}</div>"
    
    return html

# {'packet': ['{"title":"dsfds",
# "blocks":
#       [[{"type":"h1","content":"sdffsdfsdfs"},{"type":"p","content":"sdfsdfsd"}]]

#Test if user is logged out
def logout_test(test_func, redirect_url):
    def decorator(view_func):

        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            if test_func(request.user):
                return redirect(resolve_url(redirect_url))
            
            return view_func(request, *args, **kwargs)
            
        return _wrapper_view

    return decorator

def logout_required(function = None, redirect_url = None):
    actual_decorator = logout_test(
        lambda u: u.is_authenticated,
        redirect_url=redirect_url,
    )

    if function:
        return actual_decorator(function)
    return actual_decorator

#Test if user is the owner of article
def user_isauthor_test(redirect_url):
    def decorator(view_func):

        @wraps(view_func)
        def _wrapper_view(request, *args, **kwargs):
            article = Article.objects.get(id = kwargs["pk"])
            if request.user == article.author:
                return view_func(request, *args, **kwargs)
            
            return redirect(resolve_url(redirect_url))
    
        return _wrapper_view
    
    return decorator

def user_isauthor(function = None, redirect_url = None):
    actual_decorator = user_isauthor_test(
        redirect_url = redirect_url,
    )
    
    if function:
        return actual_decorator(function)
    return actual_decorator