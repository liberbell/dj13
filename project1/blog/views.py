from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article, Comment
from django.core.paginator import Paginator
from .forms import CommentForm

# Create your views here.
def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)
    page_num = request.GET.get("page")
    
    context = {
        "page_obj": paginator.get_page(page_num),
        "page_num": page_num,
    }
    
    return render(request, "blog/blogs.html", context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    
    if request.method == "POST":
        
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.author = request.user
                comment.article = obj
                comment.save()

    comments = Comment.objects.filter(article=obj)

    context = {
        "article": obj,
        "comments": comments
    }
    
    return render(request, "blog/article.html", context)