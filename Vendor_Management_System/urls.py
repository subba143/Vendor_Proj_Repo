"""Vendor_Management_System URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from vendor_management import views
from rest_framework.authtoken import views as v
from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('api',views.VendorPerformanceAPIView)
# from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    path('get-api-token/', v.obtain_auth_token, name='get-api-token'),
    path('api/vendors/', views.VendorListCreateAPIView.as_view(), name='vendor-list-create'),
    path('api/vendors/<int:pk>/', views.VendorRetrieveUpdateDestroyAPIView.as_view(), name='vendor-retrieve-update-destroy'),
    path('api/vendors/<int:pk>/performance/', views.VendorPerformanceAPIView.as_view({'get': 'retrieve'}), name='vendor-performance'),
    path('api/purchase_orders/', views.PurchaseOrderListCreateAPIView.as_view(), name='purchase-order-list-create'),
    path('api/purchase_orders/<int:pk>/', views.PurchaseOrderRetrieveUpdateDestroyAPIView.as_view(), name='purchase-order-retrieve-update-destroy'),
    path('api/historical_performances/', views.HistoricalPerformanceListCreateAPIView.as_view(), name='historical-performance-list-create'),
    path('api/historical_performances/<int:pk>/', views.HistoricalPerformanceRetrieveUpdateDestroyAPIView.as_view(), name='historical-performance-retrieve-update-destroy'),
    # path('auth-jwt/', obtain_jwt_token),
]

