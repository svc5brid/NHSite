from django.urls import path
from . import views

app_name = "Balance_Management"
urlpatterns = [
    path('index', views.index, name='index_bm'),
    path('SelectProfile', views.SelectProfile.as_view(), name="SelectProfile"),
    # Supply when select user at create profile page
    path('SelectProfile_API', views.SelectProfile_API.as_view(), name="SelectProfile_API"),
    # path('confirm_useable_profilename', views.select_user, name='confirm_useable_profilename'),
    # path('select_user1', views.select_user, name='select_user1'),
    ]