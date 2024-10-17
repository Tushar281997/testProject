from rest_framework import generics
from rest_framework.views import APIView  # For APIView base class

from rest_framework.response import Response
from rest_framework import status
from .models import VendorMaster
from .serializers import VendorMasterSerializer
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination

class VendorMasterSearchView(generics.ListAPIView):
    serializer_class = VendorMasterSerializer
    pagination_class = PageNumberPagination  # Pagination class

    def get_queryset(self):
        queryset = VendorMaster.objects.all()
        
        # Extract query parameters from request
        ap_vendor_number_lst = self.request.query_params.getlist('apVendorNumberLst[]', None)
        include_inactive_vendors = self.request.query_params.get('includeInactiveVendors', None)
        vendor_type = self.request.query_params.get('vendorType', None)
        client_group = self.request.query_params.get('clientGroup', None)
        
        # Filter by vendor numbers (if provided)
        if ap_vendor_number_lst:
            queryset = queryset.filter(ap_vendor_number__in=ap_vendor_number_lst)

        # Filter out inactive vendors if 'N' is provided
        if include_inactive_vendors == 'N':
            queryset = queryset.filter(inactive_date__isnull=True)

        # Filter by vendor type (if provided)
        if vendor_type:
            queryset = queryset.filter(vendor_type_def=vendor_type)

        # Filter by client group (if provided)
        if client_group:
            queryset = queryset.filter(client=client_group)
        
        return queryset

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)  # Use pagination

        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)  # Return paginated response
        
