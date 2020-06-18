from django.urls import path
from .views import HomeView, ArticleDetailView, AddPostView, UpdatePostView, DeletePostView, AddCategoryView, CategoryView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('post/<int:pk>', ArticleDetailView.as_view(), name="post"),
    path('addPost/', AddPostView.as_view(), name="add_post"),
    path('addCategory/', AddCategoryView.as_view(), name="add_category"),
    path('post/edit/<int:pk>', UpdatePostView.as_view(), name="update_post"),
    path('post/<int:pk>/remove', DeletePostView.as_view(), name="delete_post"),
    path('category/<str:cats>/', CategoryView, name='category')
]
