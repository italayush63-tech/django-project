from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('posts/', views.posts),
    path('posts/<int:post_id>/', views.post_detail),
    path('login/', auth_views.LoginView.as_view(template_name='myapp/login.html')),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.signup),
    path('posts/new/', views.create_post),
]