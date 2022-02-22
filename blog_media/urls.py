from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include

import users.views

urlpatterns = [
    path('', include('blog.urls')),
    path('admin/', admin.site.urls),
    path('register/', include('users.urls')),
    path('login/', auth_views.LoginView.as_view(template_name="users/login.html"), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name="users/logout.html"), name='logout'),
    path('profile/', users.views.profile, name="profile"),
]
