from django.urls import path
from . import views
from .views import HomeView, ArticleView, AddPostView, UpdatePostView, DeletePostView
urlpatterns = [
    path('account/register', views.register, name='register'),
    path('account/login', views.login, name='login'),
    path('account/logout', views.logout, name='logout'),
    path('', HomeView.as_view(), name='home'),
    path('account/article/<int:pk>', ArticleView.as_view(), name='article-detail'),
    path('account/add_post/', AddPostView.as_view(), name='add_post'),
    path('account/article/edit/<int:pk>', UpdatePostView.as_view(), name='update_post'),
    path('account/article/delete/<int:pk>', DeletePostView.as_view(), name='delete_post'),
]