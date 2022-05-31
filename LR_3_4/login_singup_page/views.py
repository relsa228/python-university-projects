from django.shortcuts import render, redirect
from .forms import RegUsersForm, LogUsersForm
from django.contrib.auth.views import LoginView
from django.views.generic.edit import CreateView


def email_aprove(request):
    return render(request, 'login_singup_page/email_aprove_page.html')


class RegistrationView(CreateView):
    success_url = 'email_aprove/'
    form_class = RegUsersForm
    template_name = 'login_singup_page/reg_page.html'


class CustLoginView(LoginView):
    form_class = LogUsersForm
    template_name = 'login_singup_page/login_page.html'

    def get_success_url(self):
        return '/./user/'
