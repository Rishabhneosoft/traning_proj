from django.urls import path
from .views import *

# from .views import RegisterAPI
# from django.contrib.auth import views as auth_views
from .views import(
    registration_view,
)
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
    path('assignment/<int:pk>/',AssignmentView.as_view(),name='assignment'),

    path('api/register/', registration_view, name='register'),
    path('login/', LoginView.as_view()),

    # path('logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]

