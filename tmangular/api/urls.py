from django.conf.urls import patterns, url, include
from rest_framework import routers
from tmangular.api import views

router = routers.DefaultRouter()
router.register(r'users', views.AccountViewSet)

urlpatterns = patterns('',
    url(r'^', include(router.urls)),
    url(r'^auth-token/$', 'rest_framework_jwt.views.obtain_jwt_token', name='authenticate-token'),
)
