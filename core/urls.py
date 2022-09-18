from django.urls import path
from .views import *
# from django.contrib.auth import views as auth_views

app_name = "core"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('learndj/', views.learn_django)
    path('signup/',RegistrationView.as_view(),name='signup'),
	# path('profile/',views.user_profile,name='profile'),
    path('login/',LoginView.as_view(),name='login'),

    path('tl/',DeshbordView.as_view(),name='tl'),
    # path('user/',UserView.as_view(),name='userhome'),
    path('about/',AboutView.as_view(),name='about'),

    path('detail/<int:pk>/',UserDetailView.as_view(),name='user-detail'),

    # path('add-traning-assign/<int:pk>/',AddView.as_view(),name='add-traning-assign'),

    path('review/',ReviewView.as_view(),name='review'),
    path('traning/<int:pk>/',TraningView.as_view(),name='traning'),


    # path('logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]