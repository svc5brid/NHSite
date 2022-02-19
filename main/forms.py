from django import forms
import re
from main.models import CustomUser

class CustomUserForm(forms.ModelForm):
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)
    class Meta:
        model = CustomUser
        fields = ("username", "email", "first_name", "last_name")
    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user
    def clean_username(self):
        username = self.cleaned_data.get("username")
        if not username:
            raise forms.ValidationError("ユーザー名を入力してください。")
        return username
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if not email:
            raise forms.ValidationError("メールアドレスを入力してください。")
        elif not re.match(r".+@.+", email):
            raise forms.ValidationError("メールアドレスを入力してください。")
        return email
    def clean_first_name(self):
        firstname = self.cleaned_data.get("first_name")
        if not firstname:
            raise forms.ValidationError("姓を入力してください。")
        return firstname
    def clean_last_name(self):
        lastname = self.cleaned_data.get("last_name")
        if not lastname:
            raise forms.ValidationError("名を入力してください。")
        return lastname