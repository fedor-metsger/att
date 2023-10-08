
from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from chain.views import FactoryViewSet, RetailerViewSet, EntrepreneurViewSet

factory_router = routers.DefaultRouter()
factory_router.register(r'factory', FactoryViewSet)

retailer_router = routers.DefaultRouter()
retailer_router.register(r'retailer', RetailerViewSet)

entrepreneur_router = routers.DefaultRouter()
entrepreneur_router.register(r'entrepreneur', EntrepreneurViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('', include(factory_router.urls)),
    path('', include(retailer_router.urls)),
    path('', include(entrepreneur_router.urls)),
]
