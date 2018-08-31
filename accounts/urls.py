from django.urls import path
from .views import FacebookLogin

app_name='accounts'

urlpatterns = [
	path('rest-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
]