from django.shortcuts import render, redirect
from django.views import View
from django.http import JsonResponse


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
        request.session["Balance-Management_Profile"] = "Test"
        return render(request, "Balance-Management/Select_Profile.html", context)
def get_profile(request):
    number1 = int(request.POST['number1'])
    number2 = int(request.POST["number2"])
    plus = number1 + number2
    minus = number1 - number2
    d = {
        'plus': plus,
        'minus': minus,
    }
    return JsonResponse(d)