from django.shortcuts import render, redirect
from django.contrib.auth.views import LoginView
from blog.models import Article
from mysite.forms import UserCreationForm, ProfileForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login

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
    
    def form_valid(self, form):
        messages.success(self.request, "logged in success")
        return super().form_valid(form)
    
    def form_invalid(self, form):
        messages.error(self.request, "can't logged in")
        return super().form_invalid(form)
    
def signup(request):
    context = {}
    
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save(commit=False)
            # user.is_active = False
            user.save()
            login(request, user)
            messages.success(request, "Registered success")
            return redirect("/")
        
    return render(request, "mysite/auth.html", context)

@login_required
def mypage(request):
    context = {}
    
    if request.method == "POST":
        form = ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()
            messages.success(request, "Registered success")
    return render(request, "mysite/mypage.html", context)