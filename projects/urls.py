from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.ProjectistView.as_view(), name='project_list'),
    path('project/create/', views.ProjectCreateView.as_view(), name='project_create')
]
