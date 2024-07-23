from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth.views import LoginView as BaseLoginView
from django.contrib import messages


class CustomLoginView(BaseLoginView):
    template_name = 'users/login_page.html'
    redirect_authenticated_user = True
    success_url = reverse_lazy('home:home')

    def form_valid(self, form):
        messages.error(self.request, 'Invalid username or password or email')
        return HttpResponseRedirect(self.success_url)

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = LoginForm
        return form_class(data=self.request.POST, **self.get_form_kwargs())


class SignupView(View):
    form = SignUpForm

    def get(self, request):
        context = {'form': self.form()}
        return render(request, template_name="users/signup_page.html", context=context)

    def post(self, request):
        form = self.form(request.POST)
        if form.is_valid():
            clean_date = form.cleaned_data
            password1, password2 = clean_date['password1'], clean_date['password2']
            username = clean_date['username']
            email = clean_date['email']
            if password1 == password2:
                User.objects.create(username=username, email=email, password=password1)
                messages.success(request, "your account has been created successfully")
                return redirect('users:login')
            else:
                messages.error(request, "Passwords arent match")
                return redirect('users:signup')
        else:
            return redirect("home:home")
