from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article(request):
    context = {}
    return render(request, "blog/article.html", context)