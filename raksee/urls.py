from django.urls import path
from . import views
urlpatterns=[
    path('register',views.register,name='register'),
    path('contact',views.contacting,name='contact'),
    path('about',views.aboutvil,name='about'),
    path('gallery',views.photos,name='gallery'),
    path('view',views.view,name='view')
]