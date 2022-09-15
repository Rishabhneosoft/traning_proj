from django.urls import path
from .views import *
app_name = "core"
urlpatterns = [
    # path('admin/', admin.site.urls),
    # path('learndj/', views.learn_django)
    path('signup/',RegistrationView.as_view(),name='signup'),
	# path('profile/',views.user_profile,name='profile'),
    path('login/',LoginView.as_view(),name='login'),


]