from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import *
from .models import *
# Create your views here.


class DemoView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        return Response({"msg": "You are Authenticated!"})


class ProductView(APIView):
    def get(self, request, format=None):
        category = self.request.query_params.get('category')
        print(category)
        if category:
            queryset = Product.objects.filter(
                category__slug=category)
            print(queryset.query)
        else:
            queryset = Product.objects.all()
        serializer = ProductSerializer(queryset, many=True)
        return Response({"count": len(serializer.data), "data": serializer.data})


class ProductByCategoryView(APIView):
    def get(self, request, format=None):
        pass
