from django.urls import path
from .views import HealthCheckView, SystemStatusView, ProjectInfoView

urlpatterns = [
    path('health/', HealthCheckView.as_view(), name='health'),
    path('status/', SystemStatusView.as_view(), name='status'),
    path('project/', ProjectInfoView.as_view(), name='project-info'),
]
