from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth import login as auth_login, authenticate
from django.shortcuts import render, redirect
from django import forms
from .models import User,Assignment,Traning,Review,Client
from .forms import RegistrationForm,LoginForm,TraningForm,AssignmentForm,TraningUpdateForm,ReviewForm,AssignmentUpdateForm,ClientForm
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.core.mail import EmailMessage,send_mail, EmailMultiAlternatives
from django.views.generic import UpdateView
from django.conf import settings
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import messages
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


def user_profile(request):
    return render(request, 'core/profile.html')


'''User Signup View'''
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
            message = "Please provide valid detail"
            messages.error(request, message)
            return render(request, "core/signup.html", {"form": form})
        return render(request, "core/signup.html", {"form": form})


'''User Login Or TL'''
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
                message = f'Hello {user.username}! You have been logged in'
                return redirect("core:tl")
            else:
                message = "Please provide valid username and password"
                messages.error(request, message)
                return redirect("core:login")


'''Deshbord Page'''
class DeshbordView(View):
    def get(self,request,*args, **kwargs):
        user = User.objects.all()
        assignment= Assignment.objects.all()
        review = Review.objects.filter(id=request.user.id)
        user = User.objects.get(id=request.user.id)
        traning = Traning.objects.filter()
        if user.User_type == 'TL':
            trainees= User.objects.filter(User_type='Tranni')
            return render(request, 'core/tl_home.html', {'user':user ,'assignment':assignment,'trainees':trainees})
        else:
            return render(request, 'core/tranie_home.html', {'user':user ,'assignment':assignment})


'''User Datail View'''
class UserDetailView(View):
    def get(self,request,*args,**kwargs):
        if request.method == "GET":
            user_id=kwargs.get('pk')
            user = User.objects.filter(pk=user_id).last()
            assignment= Assignment.objects.filter(user_id=user_id).last()
            traning = Traning.objects.filter(user_id=user_id).last()
            review = Review.objects.filter(user_id=user_id).last()
            client = Client.objects.filter(user_id=user_id).last()
            return render(request, 'core/user_detail_page.html', {'user':user,'assignment':assignment,'traning':traning,'review':review,'client':client})


'''User Assignment Detail View'''
class UserAssignmentDetailView(View):
    def get(self,request,*args,**kwargs):
        if request.method == "GET":
            user_id=kwargs.get('pk')
            user = User.objects.filter(pk=user_id).last()
            assignment= Assignment.objects.filter(user_id=user_id).last()
            traning = Traning.objects.filter(user_id=user_id).last()
            review = Review.objects.filter(user_id=user_id).last()
            client = Client.objects.filter(user_id=user_id).last()
            return render(request, 'core/user_assign_detail.html', {'user':user,'assignment':assignment,'traning':traning,'review':review,'client':client})


'''TL Detail Page'''
class TLDetailView(View):
    def get(self,request,*args,**kwargs):
        if request.method == "GET":
            user_id=kwargs.get('pk')
            user = User.objects.filter(pk=user_id).last()
            assignment= Assignment.objects.filter(user_id=user_id).last()
            traning = Traning.objects.filter(user_id=user_id).last()
            review = Review.objects.filter(user_id=user_id).last()
            client = Client.objects.filter(user_id=user_id).last()
            return render(request, 'core/tl_detail_page.html', {'user':user,'assignment':assignment,'traning':traning,'review':review,'client':client})


'''About View'''
class AboutView(View):
    def get(self, request, *args, **kwargs):
        return render(request, "core/about.html")


'''Review Perticular User '''
class ReviewView(View):
    def get(self, request, *args, **kwargs):
        user_id=kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        review=Review.objects.filter().last()
        form = ReviewForm(user)
        return render(request, "core/review.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs): 
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id) 
        form = ReviewForm(user,request.POST)  
        if form.is_valid():  
            form.save()  
        else:
            message = "Please create again"
            messages.error(request, form.errors) 
        return redirect("core:tl")


'''Add Traning Model'''
class TraningView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        form = TraningForm(user)
        return render(request, "core/traning.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        form = TraningForm(user,data=request.POST)
        if form.is_valid():
            form.save()
            body = "Hello you have assign.traning model! Please Check NeoSoft Traning Portal"
            send_mail = EmailMessage("Traning module will send",body,to=[user[0].email])
            send_mail.send()
            messages.success(self.request, ' Mail Send Successfully')
            messages.success(request, 'Successfuly Created')
        else:
            message = "Please create again"
            messages.error(request, form.errors)
        return render(request,"core/traning.html",{"form":form})

'''Add Assignment View'''
class AssignmentView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        form = AssignmentForm(user)
        return render(request, "core/assignment.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        form = AssignmentForm(user,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("core:tl")

        else:
            message = "Please create again"
            messages.error(request, form.errors)
        return render(request,"core/assignment.html",{"form":form})


'''Traning Update View'''
class TraningUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        traning=Traning.objects.filter(user=user[0]).last()
        form = TraningUpdateForm(user,initial={'user': traning.user,
        'status': traning.status,
        'Start_traning_date':traning.Start_traning_date,
        'End_traning_date':traning.End_traning_date,
        'traning_topic':traning,
        'discription':traning.discription})
        return render(request, "core/traning_update.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs): 
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id) 
        form = TraningUpdateForm(user,request.POST)  
        if form.is_valid():  
            form.save()
            messages.success(self.request, ' Mail Send Successfully')
            return redirect("core:tl")  
        return render(request, 'core/traning_update.html', {'user': user})


'''Assignment Upadte View'''
class AssignmentUpdateView(View):
    def get(self, request, *args, **kwargs):
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id)
        assignment=Assignment.objects.filter(user=user[0]).last()
        client=Client.objects.filter(user=user[0]).last()
        form = AssignmentUpdateForm(user,initial={'user': assignment.user,
        'status': status,
        'Start_traning_date':assignment.Start_traning_date,
        'End_traning_date':assignment.End_traning_date,
        'assignment_topic':assignment,
        'client':client})
        return render(request, "core/edit_assignment.html", {"form": form,"user_id":user_id})

    def post(self, request, *args, **kwargs): 
        user_id = kwargs.get('pk')
        user = User.objects.filter(pk=user_id) 
        form = AssignmentUpdateForm(user,request.POST)  
        if form.is_valid():  
            form.save() 
            messages.success(self.request, 'Updated Successfuly') 
            return redirect("core:tl")
        else:
            message = "Please create again"
            messages.error(request, form.errors)
        return render(request,"core/edit_assignment.html",{"form":form})  


'''Client Detail View'''
class ClientView(View):
    def get(self,request,*args,**kwargs):
        if request.method == "GET":
            user_id=kwargs.get('pk')
            user = User.objects.filter(pk=user_id).last()
            client= Client.objects.filter(user_id=user_id).last()
            assignment= Assignment.objects.filter(user_id=user_id).last()
            return render(request, 'core/client.html', {'client':client,'assignment':assignment})


'''API PART'''
from rest_framework import permissions
from rest_framework import views
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import RegistrationSerializer

'''User Signup API'''
@api_view(['POST',])
def registration_view(request):

    if request.method == 'POST':
        serializer = RegistrationSerializer(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']="successful registration"
            data['email'] = account.email
            data['username'] = account.username
            data['mobile_number'] = account.mobile_number
        else:
            data = serializer.errors
        return Response(data)


'''User Login API'''
class UserLoginView(views.APIView):
    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = serializers.LoginSerializer(data=self.request.data,
            context={ 'request': self.request })
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        login(request, user)
        res = {"message":"User Login Successfully"}
        return Response(data=res, status=status.HTTP_200_OK)