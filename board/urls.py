from django.urls import path

from board.views import index, PostCreate, PostDetail, RespondDelete

urlpatterns = [
    path('posts/', index, name='index'),
    path('addpost/', PostCreate.as_view(), name='addpost'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('respdelete/<int:pk>/', RespondDelete.as_view(), name='resp_delete')
]