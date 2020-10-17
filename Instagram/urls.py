from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import path, include
from Authentication import views
from  django.conf.urls.static import static
from django.conf import  settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register' ),
    path('profile/', views.profile, name='profile' ),
    path('login/', auth_views.LoginView.as_view(template_name='Authentication/login.html'), name='login' ),
    path('logout/', auth_views.LogoutView.as_view(template_name='Authentication/logout.html'), name='logout' ),
    path('', include('IG.urls') ),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)