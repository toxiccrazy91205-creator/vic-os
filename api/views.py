import psutil
import platform
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from .serializers import SystemStatusSerializer

class HealthCheckView(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        return Response({"status": "healthy", "timestamp": datetime.datetime.now().isoformat()})

class SystemStatusView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        data = {
            "status": "online",
            "version": "1.0.0-vicos",
            "uptime": str(datetime.timedelta(seconds=int(psutil.boot_time()))),
            "cpu_usage": psutil.cpu_percent(),
            "ram_usage": psutil.virtual_memory().percent,
            "os": platform.system(),
            "processor": platform.processor(),
        }
        return Response(data)

class ProjectInfoView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        # Detect project structure
        import os
        project_root = os.path.join(os.getcwd(), 'vic-os')
        recipe_path = os.path.join(project_root, 'recipes', 'recipe.yml')
        
        exists = os.path.exists(recipe_path)
        return Response({
            "project_name": "vic-os",
            "recipe_found": exists,
            "path": project_root
        })
