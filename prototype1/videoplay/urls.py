from django.urls import path, re_path
from videoplay import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.agree,name='videoplay-agree'),
    path('home/', views.home,name='videoplay-home'),
    re_path('download/', views.download,name='videoplay-download1'), 
    re_path('download2/', views.download2,name='videoplay-download2'), 
    path('temp/',views.temp, name='score-collection'),
    path('temp2/',views.temp2, name='score-collection2'),
    path('preference/',views.preference, name='score-preference'),
    path('videos/', views.play_for_single, name='videoplay-videos'),
    path('videos2/', views.play_for_double, name='videoplay-videos2')
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
