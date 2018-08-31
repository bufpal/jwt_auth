from django.contrib import admin
from django.urls import include, path

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
	path('accounts/', include('accounts.urls', namespace='accounts')),
    
	path('api-jwt-auth/', obtain_jwt_token),
	path('api-jwt-auth/refresh/', refresh_jwt_token),
	path('api-jwt-auth/verify/', verify_jwt_token),
	
	path('rest-auth/', include('rest_auth.urls')),
    path('rest-auth/registration/', include('rest_auth.registration.urls')),
]
