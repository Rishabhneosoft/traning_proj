from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
# from .form import RegistrationForm,LoginForm
from django import forms
from .forms import RegistrationForm,LoginForm
from django.views import View
from django.contrib.auth import authenticate, login, logout

# class SignupView(View):
#     def get(self,request):
#         # if response.
#         fm = RegisterForm()
#         return render(request, 'core/signup.html',{"form":fm})
#     def post(self,request):
#         if request.method == "POST":
#             form = RegisterForm(request.POST)
#             if form.is_valid():
#                 form.save()
#             return redirect("login")
#         else:
#             form = RegisterForm()
#         return render(response, "core/signup.html", {"form":fm})

from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
# class UsewrLogin(view):
#     def

# def user_login(request):
#     import pdb;pdb.set_trace()
    
#     if request.method == "POST":
#         fm = AuthenticationForm(request=request,data=request.POST)
#         if fm.is_valid():
#             uname = fm.cleaned_data['email']
#             upass = fm.cleaned_data['password']
#             user=authenticate(email=uname, password=upass)
#             if user is not None:
#                 login(request, user)
#                 return HttpResponseRedirect('/profile/')

#     else:

#         fm = AuthenticationForm()
#     return render (request,'core/login.html',{'form':fm})
# from django.urls import reverse 
# from django.views.generic import FormView
# class LoginView(FormView):
#     import pdb;pdb.set_trace()

#     form_class = AuthenticationForm
#     template_name = 'core/login.html'
#     def form_valid(self, form):
#         import pdb;pdb.set_trace()
#         email = form.cleaned_data.get('username')
#         password = form.cleaned_data.get('password')
#         user = authenticate(email=email, password=password)
        
#         # if user.is_staff and user.is_admin:
#         #     auth_login(self.request, user)
#         # else:
#         #     message = "Credentials is not valid and you are not authorised user !"
#         #     return render(self.request,'admin/login.html',{'error': message })
#         return HttpResponseRedirect(reverse('profile'))

#     def get(self, request, *args, **kwargs):
#         """Handle GET requests: instantiate a blank version of the form."""
#         if request.user.is_authenticated:
#             return HttpResponseRedirect(reverse('profile'))
#         return self.render_to_response(self.get_context_data())


# def user_login(request):
#     import pdb;pdb.set_trace()
#     if request.method == 'POST':
#         email = request.POST.get('email', '')
#         password = request.POST.get('password', '')
#         if email and password:
#             user = authenticate(email=email, password=password)
#             # user = email==email, 
#             # password = password==password
#             if user:
#                 auth_login(request, user)
#                 return redirect('profile')    
#         else:
#             message = "Wrong username and password"
#         return render(request,'core/login.html')
#     # if request.method =="GET":
#     else:
#         form = LoginForm
#         return render(request,'core/login.html',{"form":form})

def user_profile(request):
    return render(request, 'core/profile.html')


class RegistrationView(View):
    def get(self, request, *args, **kwargs):
        form = RegistrationForm()
        return render(request, "core/signup.html", {"form": form})
    def post(self, request, *args, **kwargs):
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.data["password"])
            user.save()
            messages.success(request, "User Registered Successfully")
            return redirect("core:login")
        else:
            messages.error(request, form.errors)
            return HttpResponseRedirect("core/signup/")
        return render(request, "core/signup.html", {"form": form})


class LoginView(View):
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, "core/login.html", {"form": form})

    def post(self, request, *args, **kwargs):
        form = LoginForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                # message = f'Hello {user.username}! You have been logged in'
                return redirect("core:home")
            else:
                message = "Please provide valid username and password"
                messages.error(request, message)
                return redirect("core:login")

# def user_profile(request):
#     return render(request, 'core/profile.html')