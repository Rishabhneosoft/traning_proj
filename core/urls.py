from django.urls import path
from .views import *
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
    path('assignment-update/<int:pk>/',AssignmentUpdateView.as_view(),name='assignment-update'),
    path('client/<int:pk>/',ClientView.as_view(),name='client'),



# '''API URL'''
    path('api/register/', registration_view, name='register'),
    path('api/login/', UserLoginView.as_view()),

]

