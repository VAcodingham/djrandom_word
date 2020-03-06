from django.urls import path
from . import views
from .views import redirect_random

urlpatterns = [
    path('', views.randomword),
    path('redirect_random', views.redirect_random),
    path('clear', views.clearcount)
]
