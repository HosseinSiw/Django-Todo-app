from django.shortcuts import render, redirect
from django.views import View
from .forms import LoginForm, SignUpForm
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.messages import error, success


class CustomLoginView(View):
    """
       Class-based view for handling user logins.

       This view displays the login form on GET requests and processes login attempts on POST requests.
       Upon successful authentication, the user is redirected to the home page; otherwise, an error message is displayed.
    """
    template_name = 'users/login_page.html'

    def get(self, request, *args, **kwargs):
        """
                Handles GET requests to display the login form.

                Initializes and renders the LoginForm with the login page template.
        """
        form = LoginForm()
        context = {'form': form}
        return render(request, template_name=self.template_name, context=context)

    def post(self, request, *args, **kwargs):
        """
                Handles POST requests to process login attempts.

                Validates the submitted form data, authenticates the user, logs them in if valid,
                and redirects to the home page upon success. Displays an error message if login fails.
        """
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
    """
        Class-based view for handling user signups.
        This view displays the signup form on GET requests and processes signup attempts on POST requests.
        Upon successful registration, the user is redirected to the login page; otherwise, an error message is displayed.
    """
    form = SignUpForm

    def get(self, request):

        context = {'form': self.form()}
        return render(request, template_name="users/signup_page.html", context=context)

    def post(self, request):
        """
            Handles POST requests to process signup attempts.

            Validates the submitted form data, creates a new user if valid,
            and redirects to the login page upon success. Displays an error message if signup fails.
        """
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
