from django.contrib import admin
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name="home"),
    path('blogs',views.blogs,name="blogs"),
    path('loogin',views.loogin,name="loogin"),
    path('registration/',views.registration,name="registration"),
    path('logout',views.logout_view,name="logout"),
    # path('postcomment',views.postcomment,name="postcomment"),
    path('project/<str:id>',views.personal_project_page,name="personal_project_page"),
    path('blogs/<str:unique_id>',views.user_personal_page,name="user_personal_page"),
    # path('summernote/', include('django_summernote.urls')), 
    # path("insta",views.insta,name="insta"),
]
# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)