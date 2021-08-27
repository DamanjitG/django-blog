from . import views
from .views import AboutView, PostList, PostDetail, PostCreate, PostUpdate, PostDelete
from django.urls import path

urlpatterns = [
    path('', PostList.as_view(), name='blog-homepage'),
    path('post/<int:pk>/', PostDetail.as_view(), name='post-detail'),
    path('post/new/', PostCreate.as_view(), name='post-create'),
    path('post/<int:pk>/update', PostUpdate.as_view(), name='post-update'),
    path('post/<int:pk>/delete', PostDelete.as_view(), name='post-delete'),
    path('about/', AboutView.as_view(), name='blog-about'),                    
]