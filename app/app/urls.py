from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from webapp.views import PostCreate

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name='index'),
    path('addpost', PostCreate.as_view(), name='add_post'),

    path('', include('accounts.urls'))

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) \
              + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
