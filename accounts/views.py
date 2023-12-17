from django.shortcuts import render
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import SignupForm

# Create your views here.

# Djangoでは、Model, ModelForm, Formと3種類ある
# CreateViewで定義するフォームは、ModelForm
class SignupView(CreateView):
    model         = User
    # form_classは、CreateViewの中で使うFormを指定する際に用いる
    form_class    = SignupForm
    template_name = 'accounts/signup.html'
    success_url   = reverse_lazy('index')