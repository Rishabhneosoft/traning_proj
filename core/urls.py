from django.urls import path
from .views import *

# from .views import RegisterAPI
# from django.contrib.auth import views as auth_views
from .views import(
    registration_view,
)
app_name = "core"
urlpatterns = [
    path('signup/',RegistrationView.as_view(),name='signup'),
    path('login/',LoginView.as_view(),name='login'),
    path('tl/',DeshbordView.as_view(),name='tl'),
    path('about/',AboutView.as_view(),name='about'),
    path('detail/<int:pk>/',UserDetailView.as_view(),name='user-detail'),
    # path('add-traning-assign/<int:pk>/',AddView.as_view(),name='add-traning-assign'),
    path('review/<int:pk>/',ReviewView.as_view(),name='review'),
    path('traning/<int:pk>/',TraningView.as_view(),name='traning'),
    path('assignment/<int:pk>/',AssignmentView.as_view(),name='assignment'),
    path('traning-update/<int:pk>/',TraningUpdateView.as_view(),name='traning-update'),

# '''API URL'''
    path('api/register/', registration_view, name='register'),
    path('api/login/', UserLoginView.as_view()),

]

