from django.urls import path
from django.contrib.auth.views import LoginView
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list

urlpatterns = [
    path('', post_list, name='post_list'),
    path('rust-calculator/', views.rust_calculator_view, name='rust_calculator'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)