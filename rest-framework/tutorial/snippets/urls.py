from django.conf.urls import include, url
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views


router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)


urlpatterns = format_suffix_patterns[
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
