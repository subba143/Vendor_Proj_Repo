                                                Vendor_Management_System_Documentation.md
                                                =========================================


VENDOR MANAGEMENT SYSTEM :-
________________________

The Vendor Management System is a Django-based web application designed to streamline vendor management processes for businesses.
This system allows users to manage vendor information, track purchase orders, and monitor vendor performance metrics.


FEATURES :-
---------

Create, update, and delete vendor records
Manage purchase orders, including creation, updating, and tracking
Calculate and visualize vendor performance metrics, such as on-time delivery rate, quality rating average, and fulfillment rate
User authentication and authorization to control access to sensitive data
RESTful API endpoints for seamless integration with other systems


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


SET INSTRUCTIONS :
_________________

Clone the repository : git clone https://github.com/subba143/Vendor_Proj_Repo.git
Install the required dependencies: pip install -r requirements.txt
Configure the Django settings : SECRET_KEY = 'django-insecure-#h022#-s9m_)(m+q*j)4=wbsbpjge+25q3#ezkn+nm3twgn=aq'
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'vendor_management',
    'rest_framework',
    'rest_framework.authtoken',
    'django_seed',

]


REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': ('rest_framework.authentication.TokenAuthentication',),
    'DEFAULT_PERMISSION_CLASSES': ('rest_framework.permissions.IsAuthenticated',),
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 10,
}


# JWT_AUTH={
# 'JWT_ALLOW_REFRESH':True,
# }


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


Apply migrations to create the database schema: python manage.py migrate
Create a superuser account to access the Django admin interface: python manage.py createsuperuser
Start the development server: python manage.py runserver


USAGES:
-------

Access the Django admin interface to manage vendor records and purchase orders: http://localhost:8000/admin/, http://127.0.0.1:8000/admin/
Use the provided REST API endpoints to interact with the system programmatically: http://localhost:8000/api/ ,http://127.0.0.1:8000/api.


CONTRIBUTING :
**************

Contributions are welcome! Feel free to open issues for bug reports or feature requests.
Fork the repository, make your changes, and submit a pull request for review.
