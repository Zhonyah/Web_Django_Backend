from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('addnews/', views.addnews),
    path('result/', views.result, name="result"),
    path('addnewsdata/',views.addnewsdata, name='addnewsdata'),
    path('content/',views.content),
    path('contentedit/',views.contentedit, name="contentedit"),
    path('contentupdate/',views.contentupdate, name="contentupdate"),
    path('contentdelete/',views.contentdelete, name='contentdelete'),
    path('contentshow/',views.contentshow, name="contentshow"),
    path('regisusers/',views.regisusers),
    path('regis_usersdata',views.regis_usersdata, name="regis_usersdata"),
    path('login',views.login, name="login"),
    path('logincheck',views.logincheck, name="logincheck"),
    path('logoff',views.logoff, name="logoff"),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
