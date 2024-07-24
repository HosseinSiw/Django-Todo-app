from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.messages import error, success


class CustomLoginView(View):
    template_name = 'users/login_page.html'

    def get(self, request, *args, **kwargs):
        form = LoginForm()
        context = {'form': form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            username, email, password = form.cleaned_data['username'], form.cleaned_data['email'], form.cleaned_data['password']
            user = authenticate(password=password, email=email)
            if user is not None:
                login(request, user)
                success(request, f'You are now logged in! as {request.user.username}')
                return redirect('home:home')
            else:
                error(request, 'Incorrect username or password!')
                return redirect('users:login')


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
                User.objects.create_user(username=username, email=email, password=password1)
                success(request, "your account has been created successfully")
                return redirect('users:login')
            else:
                error(request, "Passwords arent match")
                return redirect('users:signup')
        else:
            return redirect("home:home")
