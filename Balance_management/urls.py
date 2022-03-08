from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index_bm'),
    path('SelectProfile', views.SelectProfile.as_view(), name="SelectProfile")
    ]