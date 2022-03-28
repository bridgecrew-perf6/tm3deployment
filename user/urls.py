from . import views
from django.urls import path, re_path, include


urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('mah_user_login', views.mah_user_login, name='mah_user_login'),
    # path('signup', views.signup, name='signup'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('profile_update', views.profile_update, name='profile_update'),
    path('signup', views.signup, name='signup'),

]
