
from django.contrib import admin
from django.urls import path
from myapp import views 
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/',views.HelloView.as_view(),name='Hello'),
    path('api-token-auth/',obtain_auth_token,name='api-token-auth'),
]

#Generated token 726ccc00cec5fc25f26d84d5f0a7ebe41e31548c for user gowthaman