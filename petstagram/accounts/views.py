# ACCOUNTS VIEWS
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic as views

from petstagram.accounts.forms import UserCreateForm

UserModel = get_user_model()

class SignInView(LoginView):
    template_name = 'accounts/login-page.html'


class SignUpView(views.CreateView):
    template_name = 'accounts/register-page.html'
    model = UserModel
    form_class = UserCreateForm
    success_url = reverse_lazy('index')

def delete_user(request, pk):
    return render(request, 'accounts/profile-delete-page.html')


def details_user(request, pk):
    return render(request, 'accounts/profile-details-page.html')


def edit_user(request, pk):
    return render(request, 'accounts/profile-edit-page.html')