from django.shortcuts import render
from django.views.generic import TemplateView, FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth.models import User

from django.urls import reverse_lazy

from django import forms
# Create your views here.
class SiteLoginView(LoginView):
    template_name = 'login.html'

class RegisterForm(UserCreationForm):
    # email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email']
        field_classes = {'username': UsernameField} 
class SiteRegisterView(FormView):
    template_name = 'register.html'
    form_class = RegisterForm
    def form_valid(self, form):
        data = form.cleaned_data
        User.objects.create_user(username=data['username'], email=data['email'], password=data['password1'])
        return super().form_valid(form)
    success_url = reverse_lazy('login')
     
class EditProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'
