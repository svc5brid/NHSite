from django.shortcuts import render, redirect
from main.forms import CustomUserForm
from django.contrib.auth import authenticate, login

# Create your views here.

# ホームぺージ。
def index(request):
    context = {}
    # 表示するアプリ集
    apps = []
    context["apps"] = apps
    return render(request, "index.html", context)


def signup(request):
    if request.method == "POST":
        form = CustomUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            input_username = form.cleaned_data["username"]
            input_password = form.cleaned_data["password1"]
            # ユーザーを認証する
            new_user = authenticate(username=input_username, password=input_password) 
            if new_user is not None:
                # ユーザーをログイン状態にする
                login(request, new_user)
                return redirect("index")
    else:
        form = CustomUserForm()
    return render(request, "SignUp.html", {"form": form})