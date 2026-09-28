from django.urls import path, include
from . import views

urlpatterns = [    
    path("tags/<slug:pk>/", views.tags),
    path('<slug:pk>/', views.article),
    path('', views.index)
]
