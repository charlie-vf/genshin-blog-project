"""genshin URL Configuration"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('', include('blog.urls'), name='blog_urls'),
    path('accounts/', include('allauth.urls')),
]

handler404 = 'genshin.views.handler404'
handler500 = 'genshin.views.handler500'
handler403 = 'genshin.views.handler403'
handler405 = 'genshin.views.handler405'
