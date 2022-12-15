from django.urls import path

from profil.views import index

urlpatterns = [
    path('', index, name='index')
]