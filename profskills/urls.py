from django.urls import path

from profskills import views

# app_name = "topics"

urlpatterns = [
    path('topics/get_all/', views.TopicViewSet.as_view(), name='get_all_topics'),
    path('topics/get_by_name/<str:name>/', views.TopicViewSet.as_view({'get': 'get_by_name'}), name='get_by_name'),
]