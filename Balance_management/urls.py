from django.urls import path
from . import views

app_name = "Balance_Management"
urlpatterns = [
    path('index', views.index, name='index_bm'),
    path('SelectProfile', views.SelectProfile.as_view(), name="SelectProfile"),
    path('get_profile', views.get_profile, name="get_profile")
    ]