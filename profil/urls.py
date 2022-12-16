from django.urls import path, include

from profil.views import index, Register, confirm_email

urlpatterns = [
    path('', include('django.contrib.auth.urls')),
    path('home/', index, name='index'),
    path('register', Register.as_view(), name='register'),
    path('confirm/', confirm_email, name='confirm')
]