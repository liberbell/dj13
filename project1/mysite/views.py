from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def index(request):
    
    objs = Article.objects.all()[:3]
    context = {
        "title": "Really site",
        "articles": objs,
    }
    return render(request, "mysite/index.html", context)

# def login(request):
#     context = {
        
#     }
#     if request.method == "POST":
#         context["req"] = request.POST
        
#     return render(request, "mysite/login.html", context)

class Login(LoginView):
    template_name = "mysite/auth.html"
    
def signup(request):
    context = {}
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            messages.success(request, "Registered success")
            return redirect("/")
        
    return render(request, "mysite/auth.html", context)