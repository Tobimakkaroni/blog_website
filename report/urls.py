from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('report/', views.report_view, name='report'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)