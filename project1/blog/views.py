from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def article(request, pk):
    context = {
        "pk": pk
    }
    return render(request, "blog/article.html", context)