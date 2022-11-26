from . import views
from django.urls import path


urlpatterns = [
    # url for index.html template view
    path('', views.PostList.as_view(), name='home'),
    # path('add_post/', views.AddPost.as_view(), name='add_post'),
    path('create_post', views.CreatePost, name="create_post"),
    path('update_post/<slug:slug>', views.UpdatePost.as_view(), name='update_post'),
    path('delete_post/<slug:slug>', views.DeletePost.as_view(), name='delete_post'),
    path('category/<str:categories>', views.Category, name='category'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
