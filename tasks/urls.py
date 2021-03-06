from django.urls import path
from . import views

app_name = "tasks" 

urlpatterns = [
	path('', views.index, name='index'),
	path('list/', views.TaskListView.as_view(), name='list'),
	path('create/', views.TaskCreateView.as_view(), name='create'),
	path('completed/<int:uid>', views.completed_tasks, name='complete'),
	path('delete/<int:uid>', views.delete_task, name='delete'),
	path('add-task/', views.add_task, name='api-add-task'),
	path('details/<int:pk>', views.TaskDetailsView.as_view(), name="details"),
	path('edit/<int:pk>', views.TaskEditView.as_view(), name="edit"),
	path('export/', views.TaskExportView.as_view(), name="export"),
]