from django.urls import path
from . import views
urlpatterns = [
    path('', views.posts, name='posts'),
    path('create', views.create, name='create' ),
    path('<int:pk>', views.NewsDetail.as_view(), name='new-detail'),
    path('<int:pk>/update', views.NewsUpdate.as_view(), name='update')
]