from django.urls import path, include
from rest_framework.routers import DefaultRouter
from forms.views import FormViewSet
from responses.views import ResponseViewSet
from analytics.views import form_analytics
from django.shortcuts import redirect
from django.contrib import admin
from django.urls import path
from forms import views  # Adjust the import based on your app name.

router = DefaultRouter()
router.register(r'forms', FormViewSet, basename='form')
router.register(r'responses', ResponseViewSet, basename='response')

def redirect_to_api(request):
    return redirect('/api/')

urlpatterns = [
    path('', redirect_to_api),
    path('api/', include(router.urls)),
    path('api/forms/<int:form_id>/analytics/', form_analytics, name='form-analytics'),
    path('admin/', admin.site.urls),
]
