from django.urls import path
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeletView, UserPostListView
from . import views

urlpatterns = [
    path('', PostListView.as_view(), name='blog-home'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    # path('', views.home, name='blog-home'), for function based views we use this url
    path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeletView.as_view(), name='post-delete'),
    path('about/', views.about, name='blog-about'),

]


# Note: class based views looks for templates in the form <app>/<model>_<viewtype>.html
