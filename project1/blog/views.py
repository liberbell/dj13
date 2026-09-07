from django.shortcuts import render
from django.http import HttpResponse
from blog.models import Article
from django.core.paginator import Paginator

# Create your views here.
def index(request):
    objs = Article.objects.all()
    paginator = Paginator(objs, 2)
    page_num = request.Get.get("page")
    
    context = {
        "page_obj": paginator.get_page(page_num),
        "page_num": page_num,
    }
    
    return render(request, "blog/blogs.html", context)

def article(request, pk):
    obj = Article.objects.get(pk=pk)
    
    context = {
        "article": obj
    }
    
    return render(request, "blog/article.html", context)