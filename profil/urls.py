from django.urls import path, include

from profil.views import index, Register

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', index, name='index'),
    path('register', Register.as_view(), name='register')
]