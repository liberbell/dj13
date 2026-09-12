from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def index(request):
    
    objs = Article.objects.all()[:3]
    context = {
        "title": "Really site",
        "articles": objs,
    }
    return render(request, "mysite/index.html", context)

def login(request):
    context = {
        
    }
    if request.method == "POST":
        context["req"] = request.POST
        
    return render(request, "mysite/login.html", context)