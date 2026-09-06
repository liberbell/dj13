from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article

# Create your views here.
def article(request, pk):
    obj = Article.objects.get(pk=pk)
    
    context = {
        "pk": pk
    }
    
    return render(request, "blog/article.html", context)