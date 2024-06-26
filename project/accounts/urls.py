from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static
app_name = "accounts"
urlpatterns = [
    path('login/', login, name="login"),
    path('logout/', logout, name="logout"),
    path('signup/', signup1, name="signup1"),
    path('signup2/', signup2, name="signup2"),
    path('signup3/', signup3, name="signup3"),
    path('signup4/', signup4, name="signup4"),
    path('idpasswordfind/', idpasswordfind, name="idpasswordfind"),
    path('idfindv1/', idfindv1, name="idfindv1"),
    path('idfindv2/', idfindv2, name="idfindv2"),
    path('passwordfindv1/', passwordfindv1, name="passwordfindv1"),
    path('passwordfindv2/', passwordfindv2, name="passwordfindv2"),
    path('passwordfindv3/', passwordfindv3, name="passwordfindv3"),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)