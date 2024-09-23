from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.index, name='index'),
    path('blog/',views.blog, name='blog'),
    path('blog/<int:pk>',views.posting, name='posting'),
    #          <자료형:파라미터이름> 데이터를 views로 보내는 기능
    path('blog/new_post/', views.new_post, name='new_post'),
    path('blog/<int:pk>/remove', views.remove_post, name='remove_post'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# 위에 rlpatterns 안에 static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT), 로 넣는거와 같음