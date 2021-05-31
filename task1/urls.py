from django.urls import include,path
from task1 import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register('task', views.TaskViewSet)

urlpatterns=[path('', views.signup,name='signup'),
     path('signup', views.signup,name='signup'),
     path('login/signin', views.signin,name='signin'),
     path('signin', views.signin,name='signin'),
     path('task', views.task_details,name='task_details'),
     path('sam', views.exp,name='exp'),
     path('api', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
    ]