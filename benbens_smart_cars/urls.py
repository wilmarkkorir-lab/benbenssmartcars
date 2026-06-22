from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate
from django.http import JsonResponse
import json

def admin_login(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            username = data.get('username', '')
            password = data.get('password', '')
            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_staff:
                return JsonResponse({'token': 'authenticated', 'username': user.username})
            else:
                return JsonResponse({'error': 'Invalid credentials'}, status=401)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=400)
    return JsonResponse({'error': 'Method not allowed'}, status=405)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', admin_login),
    path('api/', include('cars.urls')),
    path('api/', include('customers.urls')),
    path('api/', include('sales.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
