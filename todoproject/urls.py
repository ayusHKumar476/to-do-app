from django.contrib import admin
from django.urls import path, include
from tasks import views as task_views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', task_views.signup_view, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    path('', task_views.task_list, name='task_list'),
    path('profile/', task_views.profile_view, name='profile'),
    path('task/create/', task_views.task_create, name='task_create'),
    path('task/<int:pk>/edit/', task_views.task_update, name='task_update'),
    path('task/<int:pk>/delete/', task_views.task_delete, name='task_delete'),
]
