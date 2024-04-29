from django.contrib import admin
from django.urls import path, include
from django_comments_xtd import urls as django_comments_xtd_urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')),
    path('', include('rust.urls')),
    path('', include('clicker.urls')),
    path('comments/', include(django_comments_xtd_urls)),
]
