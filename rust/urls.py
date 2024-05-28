from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import index

urlpatterns = [
    path('', index, name='index'),
    path('rust-calculator/', views.rust_calculator_view, name='rust_calculator'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)