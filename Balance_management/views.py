from django.shortcuts import render, redirect
from django.views import View

def get_profile(request):
    # 下記情報を使用して、その人が利用可能なプロファイル一覧をリストで返す
    # request.user()
    return ["p1", "p2", "p3", "p4"]
    
# Create your views here.
def index(request):
    context = {}
    # 表示するアプリ集
    if not "Balance-Management_Profile" in request.session:
        return redirect("SelectProfile")
    
    return render(request, "Balance-Management/index.html", context)

class SelectProfile(View):
    def get(self, request):
        context = {}
        context["profile"] = get_profile(request)
        request.session["Balance-Management_Profile"] = "Test"
        return render(request, "Balance-Management/ProfileSelecter.html", context)
    