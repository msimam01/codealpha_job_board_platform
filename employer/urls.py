from django.urls import path
from . import views

app_name = 'employer'

urlpatterns = [
    path('', views.JobListView.as_view(), name='jobs'),
    path('create/', views.JobCreateView.as_view(), name='jobs-create'),
    path('single/<int:pk>/', views.JobSingleView.as_view(), name='jobs-single'),
]
