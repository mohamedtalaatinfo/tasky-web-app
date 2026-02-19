from . import views
from django.urls import path



urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),
    path('add-task/', views.AddTaskView.as_view(), name='add-task')
]