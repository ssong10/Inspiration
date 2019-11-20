from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm

class CustomUserCreationForm(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-5 text-small',
        'placeholder': '아이디'
        }), label='')
    first_name = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-5 text-small',
        'placeholder': '성명'
        }), label='')
    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control mb-5 text-small',
        'placeholder': '이메일'
        }), label='')
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-3 text-small',
        'placeholder': '비밀번호'
        }), label='')
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-5 text-small',
        'placeholder': '비밀번호 확인'
        }), label='')
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'email','password1','password2')
        helptext=''


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control mb-3 text-small',
        'placeholder': '사용자 이름'
        }), label='')
    password = forms.CharField(widget=forms.PasswordInput(attrs={
        'class': 'form-control mb-5 text-small',
        'placeholder': '비밀번호'
        }), label='')
    class Meta:
        model = get_user_model()
        fields = ('username','password')
        
class CustomUserChangeForm(UserChangeForm):
    class Meta:
        model = get_user_model()
        fields = ('last_name', 'first_name',  'email')

