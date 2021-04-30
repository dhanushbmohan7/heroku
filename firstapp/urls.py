from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns=[
    path('',views.index,name='index'),
    path('second/',views.second,name='second'),
    path('photos/',views.photos,name='photos'),
    path('profile/<id>/',views.profile,name='profile'),
    path('search',views.search,name='search'),
     path('notif',views.notif,name='notif')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
