from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.response import Response
from vendor_management.models import Vendor, PurchaseOrder, HistoricalPerformance
from vendor_management.serializers import VendorSerializer, PurchaseOrderSerializer, HistoricalPerformanceSerializer

# Create your views here.

class VendorListCreateAPIView(generics.ListCreateAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer

class VendorRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer


from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions,DjangoModelPermissionsOrAnonReadOnly
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination, CursorPagination

class VendorPerformanceAPIView(ModelViewSet):
    queryset = Vendor.objects.all()
    serializer_class = VendorSerializer
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    permission_classes = [AllowAny]
    pagination_class = PageNumberPagination



    def retrieve(self, request, pk=None):
        instance = self.get_object()
        instance.update_performance_metrics()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)


class PurchaseOrderListCreateAPIView(generics.ListCreateAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer

class PurchaseOrderRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = PurchaseOrder.objects.all()
    serializer_class = PurchaseOrderSerializer


class HistoricalPerformanceListCreateAPIView(generics.ListCreateAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer

class HistoricalPerformanceRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = HistoricalPerformance.objects.all()
    serializer_class = HistoricalPerformanceSerializer



from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view

@api_view(['POST'])
def generate_token(request):
    user = request.user
    if user:
        token, created = Token.objects.get_or_create(user=user)
        return Response({'token': token.key})
    else:
        return Response({'error': 'User not found'}, status=400)



from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from .models import Vendor, PurchaseOrder
from .serializers import VendorSerializer, PurchaseOrderSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

@swagger_auto_schema(method='get', operation_description="Get list of vendors", responses={200: openapi.Response("List of vendors", VendorSerializer(many=True)),})
@swagger_auto_schema(method='post', operation_description="Create a new vendor", request_body=VendorSerializer)
@api_view(['GET', 'POST'])
@permission_classes([])
def vendor_list_create(request):
    if request.method == 'GET':
        vendors = Vendor.objects.all()
        serializer = VendorSerializer(vendors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = VendorSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@swagger_auto_schema(method='get', operation_description="Retrieve a specific vendor", responses={200: openapi.Response("Vendor details", VendorSerializer)})
@swagger_auto_schema(method='put', operation_description="Update a specific vendor", request_body=VendorSerializer)
@swagger_auto_schema(method='delete', operation_description="Delete a specific vendor")
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([])
def vendor_retrieve_update_destroy(request, pk):
    try:
        vendor = Vendor.objects.get(pk=pk)
    except Vendor.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = VendorSerializer(vendor)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = VendorSerializer(vendor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        vendor.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
