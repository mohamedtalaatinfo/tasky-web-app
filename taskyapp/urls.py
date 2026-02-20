from . import views
from django.urls import path



urlpatterns = [
    path('', views.IndexView.as_view(), name='home'),
    path('<int:pk>/', views.TaskDetailsView.as_view(), name='task-details'),
    path('add-task/', views.AddTaskView.as_view(), name='add-task'),
    path('complished-task/', views.ComplishedTasksView.as_view(), name='task-done'),
    path('comlished-list/', views.ComplishedListView.as_view(), name='complished-list'),
    path('<str:pk>/complished-details/', views.ComplishedDetailsView.as_view(), name='complished-details')
]
