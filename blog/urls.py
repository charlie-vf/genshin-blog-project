from . import views
from django.urls import path


urlpatterns = [
    # url for index.html template view
    path('', views.PostList.as_view(), name='home'),
]
