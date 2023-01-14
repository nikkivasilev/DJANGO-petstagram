from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UsernameField

UserModel = get_user_model()


class UserCreateForm(UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
        field_classes = {
            'username': UsernameField, }
