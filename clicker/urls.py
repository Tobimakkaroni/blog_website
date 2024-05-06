from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blog.views import post_list
from django.urls import path
from .views import update_counter
from .views import get_counter

urlpatterns = [
    path('', post_list, name='post_list'),
    path('clicker/', views.clicker_view, name='clicker'),
    path('update_counter/', update_counter, name='update_counter'),
    path('get_counter/', get_counter, name='get_counter'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    
