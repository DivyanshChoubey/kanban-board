from django.urls import path

from service.views import *

urlpatterns = [
    path('TaskCreate', TaskCreateView.as_view(), name='task-create'),
    path('TaskGet', TaskGetView.as_view(), name='task-get'),
    path('TaskUpdate', TaskUpdateView.as_view(), name='task-update')
]
