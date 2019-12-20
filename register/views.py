from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import UserInfo
from django.contrib.auth.forms import UserCreationForm
# Create your views here.from django.views.generic import TemplateView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.views.generic import TemplateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login
from .forms import SignUpForm, UserInfoForm


def thanks(request):
    return render(request, 'thanks.html')


def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.profile.birth_date = form.cleaned_data.get('birth_date')
            user.save()
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('info')
    else:
        form = SignUpForm()
    return render(request, 'register.html', {'form': form})

@login_required
def userinfoview(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST)

        if form.is_valid():
            userinfo = form.save(commit = False)

            userinfo.user = request.user
            userinfo.save()

            return redirect("thanks")
    else:
        form = UserInfoForm()
        context = {"form":form}
        return render(request, "info.html", context)