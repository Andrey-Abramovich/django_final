from django.urls import path

from board.views import PostCreate, PostDetail, RespondDelete, PostUpdate, respond_update, Posts

urlpatterns = [
    path('posts/', Posts.as_view(), name='index'),
    path('addpost/', PostCreate.as_view(), name='addpost'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post_detail'),
    path('respdelete/<int:pk>/', RespondDelete.as_view(), name='resp_delete'),
    path('post_update/<int:pk>/', PostUpdate.as_view(), name='post_update'),
    path('respond/active/<int:pk>/', respond_update, name='respond_activate')
]