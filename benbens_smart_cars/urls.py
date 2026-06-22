from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import authenticate
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import json

@csrf_exempt
@require_http_methods(['POST'])
def admin_login(request):
    try:
        data = json.loads(request.body)
        username = data.get('username', '').strip()
        password = data.get('password', '').strip()
        user = authenticate(request, username=username, password=password)
        if user is not None and (user.is_staff or user.is_superuser):
            return JsonResponse({'token': 'authenticated', 'username': user.username})
        else:
            return JsonResponse({'error': 'Invalid credentials'}, status=401)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/auth/login/', admin_login),
    path('api/', include('cars.urls')),
    path('api/', include('customers.urls')),
    path('api/', include('sales.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
