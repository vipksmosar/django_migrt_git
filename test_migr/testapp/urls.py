from django.urls import path, include
from . import views
from django.conf import urls
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
urlpatterns = [
    path(r'', views.index, name='index'),
    path(r'salary/', views.SalaryListView.as_view(), name='salary'),
    path(r'salary/(?P<pk>\d+', views.SalaryDetailView.as_view(), name='salary_detail'),
    path('api/', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
   # path('start_scripts/', include(router.register(r'test_migrate', views.Migrate_test)))
]


