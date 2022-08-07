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
        context["Profile"] = [
            {"id" : "000111222333", "name":"Profile_Test1"},
            {"id" : "111222333444", "name":"Profile_Test2"},
            ]
        context["UserList"] = [
            {"id":"0070200366", "name":"UserA"},
            {"id":"0070200367", "name":"UserB"},
            {"id":"0070200368", "name":"UserC"},
        ]
        request.session["Balance-Management_Profile"] = "Test"
        return render(request, "Balance-Management/Select_Profile.html", context)
class SelectProfile_API(View):
    def post(self, request):
        API_type = request.POST["type"]
        if API_type == "get_user":
            json = self.select_user(request)
        elif API_type == "confirm_name":
            json = self.confirm_useable_profilename(request)
        return JsonResponse(json)
    def select_user(self, request) -> list:
        user1 = request.POST['user1']
        # check record exists
        if user1 in []:
            pass
        user2 = {
            "0070200366":{"id":"0070200366", "name":"UserA"},
            "0070200367":{"id":"0070200367", "name":"UserB"},
            "0070200368":{"id":"0070200368", "name":"UserC"},
        }
        del user2[user1]
        user2 = list(user2.values())
        # if user1 == "UserA":
        #     user2 = [
        #         {"id":"0070200367", "name":"UserB"},
        #         {"id":"0070200368", "name":"UserC"},
                
        #         ]
        # else:
        #     user2 = [
        #         {"id":"0070200366", "name":"UserA"},
        #         {"id":"0070200368", "name":"UserC"},
                
        #         ]
        # return other user
        d = {
            "User2": user2
        }
        return d
    def confirm_useable_profilename(self, request) -> bool:
        profile_name = request.POST["name_profile"]
        # if inputted profile name already exists at db, return false because duplicate is not supported
        if profile_name in ["Used_Test"]:
            d = {
                "judge": False
            }
            return d
        else:
            d = {
                "judge": True
            }
            return d
