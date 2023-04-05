# users/forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm, UsernameField
from .models import CustomUser, Category, Question


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = UsernameField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'qwer', 'id': 'a'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-control',
            'placeholder': 'qwerqwer',
            'id': 'c',
        }
))

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(
        max_length=255,
        label="username",
        widget=forms.TextInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'username',
            'id': 'a'
        }
        )
    )
    email = forms.CharField(
        max_length=255,
        label="email",
        widget=forms.TextInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'email',
            'id': 'b'
        }
        )
    )
    password1 = forms.CharField(
        label="password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'password1',
            'id': 'b'
        }
        )
    )
    password2 = forms.CharField(
        label="repeat password",
        widget=forms.PasswordInput(attrs={
            'class': 'w-100 form-control',
            'placeholder': 'repeat password',
            'id': 'c'

        }
        )
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        fields = ('username', 'email')


class CategoryForm(forms.ModelForm):

    class Meta:
        model = Category
        fields = "__all__"


class AddQuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['title', 'body', 'category']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.ModelChoiceField({'class': 'form-control'})
        }
