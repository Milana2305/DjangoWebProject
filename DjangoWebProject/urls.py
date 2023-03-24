"""
Definition of urls for DjangoWebProject.
"""

from datetime import datetime
from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from app import forms, views
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.views.static import serve


urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('links/', views.links, name='links'),
    path('newpost/', views.newpost, name='newpost'),
    path('videopost/', views.videopost, name='videopost'),
    url(r'^media/(?P<path>.*)$',serve, {'document_root': settings.MEDIA_ROOT}),
    path('blog', views.blog, name='blog'),
    re_path(r'^(?P<parametr>\d+)/$', views.blogpost, name='blogpost'),
    path('anketa/', views.anketa, name='anketa'),
    path('registration/', views.registration, name='registration'),
    path('login/',
         LoginView.as_view
         (
             template_name='app/login.html',
             authentication_form=forms.BootstrapAuthenticationForm,
             extra_context=
             {
                 'title': 'Авторизация',
                 'year' : datetime.now().year,
             }
         ),
         name='login'),
    path('logout/', LogoutView.as_view(next_page='/'), name='logout'),
    path('admin/', admin.site.urls),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += staticfiles_urlpatterns()
