# from django.contrib import admin
# from django.urls import path
# # from core import views
# from core.views import *

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     # path("register/",register, name="register"),  # <-- added
#     # path('login/',views.user_login,name='login'),
#     path('login/',LoginView.as_view(),name='login'),

#     path('signup/',RegistrationView.as_view(),name='signup'),
# 	path('profile/',views.user_profile,name='profile'),

# ]


from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('core.urls')),
    # path('client/', include('sysapp.client.urls')),
    # path('question/', include('sysapp.question .urls')),
    # path('logout/', auth_views.logout, {'next_page': '/login/'}, name='logout'),
]