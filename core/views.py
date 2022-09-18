from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
# from .form import RegistrationForm,LoginForm
from django import forms
from .models import User,Assignment,Traning,Review
from .forms import RegistrationForm,LoginForm,TraningForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage,send_mail, EmailMultiAlternatives
from django.views.generic import UpdateView

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
                return redirect("core:tl")
            else:
                message = "Please provide valid username and password"
                messages.error(request, message)
                return redirect("core:login")

# def user_profile(request):
#     return render(request, 'core/tl_home.html')
class DeshbordView(View):
    def get(self,request,*args, **kwargs):
        user = User.objects.all()

        assignment= Assignment.objects.all()
        review = Review.objects.filter(id=request.user.id)
        user = User.objects.get(id=request.user.id)
        if user.User_type == 'TL':
            trainees= User.objects.filter(User_type='Tranni')

            return render(request, 'core/tl_home.html', {'user':user ,'assignment':assignment,'trainees':trainees})
        else:
            return render(request, 'core/tranie_home.html', {'user':user ,'assignment':assignment})


class UserDetailView(View):
    def get(self,request,*args,**kwargs):
        if request.method == "GET":
            user = User.objects.filter(pk=request.user.id).last()
            # user_id = user.objects.get(id=request.user.id)
            user_id=kwargs.get('pk')
            assignment= Assignment.objects.filter(user_id=user_id)
            traning = Traning.objects.filter(user_id=user_id)
            review = Review.objects.filter(user_id=user_id)
            if user.User_type == 'Tranni':
                return render(request, 'core/user_detail_page.html', {'user':user ,'assignment':assignment,'traning':traning,'review':review})
            else:
                return render(request, 'core/user_detail_page.html', {'user':user,'assignment':assignment,'traning':traning,'review':review})


# class UserUpdateView(UpdateView):
#     model = User
#     form_class = PropertyUpdateForm
#     template_name = "property_update_form.html"
#     # success_url = reverse_lazy('property_detail')
#     def get_success_url(self, **kwargs):
#         return ('/artical/'+str(self.kwargs['pk'])+'/') 


class AboutView(View):
    def get(self, request, *args, **kwargs):
        # form = Form()
        return render(request, "core/about.html")

# class AddView(View):
#     def get(self, request, *args, **kwargs):
        
#         user = User.objects.filter(pk=request.user.id).last()
#         user_id=user.pk
#         return render(request, "core/add_traning_assign.html",{'user_id':user_id})

class ReviewView(View):
    def get(self, request, *args, **kwargs):
        if request.method == "GET":
            user = User.objects.filter(pk=request.user.id).last()
            # user_id = user.objects.get(id=request.user.id)
            user_id=kwargs.get('pk')
            assignment= Assignment.objects.filter(user_id=user_id)
            # traning = Traning.objects.filter(user_id=user_id)
            review = Review.objects.filter(user_id=user_id)
            # if user.User_type == 'Tranni':
            #     return render(request, 'core/user_detail_page.html', {'user':user ,'assignment':assignment,'traning':traning,'review':review})
            # else:
            #     return render(request, 'core/user_detail_page.html', {'user':user,'assignment':assignment,'traning':traning,'review':review})
            return render(request, "core/review.html",{'assignment':assignment,'review':review,'user':user})

# class TraningUpdateView(UpdateView):
#     model = Traning
#     form_class = TraningForm
#     template_name = ".html"
#     # success_url = reverse_lazy('property_detail')
#     def get_success_url(self, **kwargs):


#         return ('/artical/'+str(self.kwargs['pk'])+'/') 

class TraningView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id).last()
        data = {'user' : user.username}
        form = TraningForm(initial=data)
        return render(request, "core/traning.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs):
        form = TraningForm(data=request.POST)
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id).last()
        if form.is_valid():
            form.data._mutable = True
            form.data['user'] = user
            form.data._mutable = False
            form.save()
            body = "this is OTP "+password+""
            send_mail = EmailMessage("Traning module will send",body,settings.FROM_EMAIL,to=[user.email])
            send_mail.send()
            messages.success(self.request, 'Check Password In Mail')
        else:
            message = "Please create again"
            form.error(request, message)
        return render(request,"core/traning.html",{"form":fm})




        # fm = (request.POST)
        # if form.is_valid():
        #     form.save()
        # send_mail = EmailMessage("",body,settings.FROM_EMAIL,to=[user.email])
        # send_mail.send()
        # messages.success(self.request, 'Check ')
        # if form.is_valid():
        #     user = form.save(commit=False)
            # user = authenticate(username=username, password=password)
            # if user is not None:
            #     login(request, user)
                # message = f'Hello {user.username}! You have been logged in'
            # else:
            #     message = "Please provide valid username and password"
            #     messages.error(request, message)
            #     return redirect("core:login")


# def post(self,request):
#     try:
#         if request.method == 'POST':
#             email = request.POST['email']
#             # try:
#             user = User.objects.get(email=email)
#             # except Exception as e:
#             #     messages.error(self.request, 'Email Not Exist')
#             #     return HttpResponseRedirect('/forgot-password/')
#             password = User.objects.make_random_password(length=8, allowed_chars='123456789')
#             user.set_password(password)
#             user.save()
#             body = "this is OTP "+password+""
#             send_mail = EmailMessage("Forgot password",body,settings.FROM_EMAIL,to=[user.email])
#             send_mail.send()
#             messages.success(self.request, 'Check Password In Mail')
#             return HttpResponseRedirect('/login/')
#     except Exception as e:
#             messages.error(request, e)
#             return HttpResponseRedirect('/forgot_password/')

# class RegistrationView(View):
#     def get(self, request, *args, **kwargs):
#         form = RegistrationForm()
#         return render(request, "core/signup.html", {"form": form})
#     def post(self, request, *args, **kwargs):
#         form = RegistrationForm(data=request.POST)
#         if form.is_valid():
#             user = form.save(commit=False)
#             user.set_password(form.data["password"])
#             user.save()
#             messages.success(request, "User Registered Successfully")
#             return redirect("core:login")
#         else:
#             messages.error(request, form.errors)
#             return HttpResponseRedirect("core/signup/")
#         return render(request, "core/signup.html", {"form": form})



'''API PART'''

from rest_framework import generics, permissions
from rest_framework.response import Response
from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer

# Register API
class RegisterAPI(generics.GenericAPIView):
    serializer_class = RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        return Response({
        "user": UserSerializer(user, context=self.get_serializer_context()).data,
        "token": AuthToken.objects.create(user)[1]
        })