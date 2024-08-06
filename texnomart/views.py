from django.http import JsonResponse
from rest_framework import status,viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.authentication import BaseAuthentication,SessionAuthentication,TokenAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from django.contrib.auth.models import User
from texnomart.models import Category,Product,Comment,Attribute,AttributeValue,ProductAttribute
from texnomart.serializers import ProductModelSerializer,CategoryModelSerializer,CategoryDetailModelSerializer,AttributeKeySerializer,AttributeValueSerializer,ProductAttributesSerializer
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
# Create your views here.

# For Category Section
class CategoryList(generics.ListAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    filter_backends = [DjangoFilterBackend]
    
    filterset_fields = ['created_at']
    search_fields = ['category_name']


    @method_decorator(cache_page(20))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)


class CategoryDetail(generics.RetrieveAPIView):
    permission_classes = [AllowAny]
    serializer_class = CategoryDetailModelSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'


# CRUD
class CategoryAdd(generics.CreateAPIView):
    
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()


class CategoryDelete(generics.DestroyAPIView):
    
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'

class CategoryListCreate(generics.ListCreateAPIView):
    
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()

class CategoryChange(generics.UpdateAPIView):
    
    serializer_class = CategoryModelSerializer
    queryset = Category.objects.all()
    lookup_field = 'slug'

#  For Product section

class ProductList(generics.ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    
    filterset_fields = ['created_at']
    search_fields = ['product_name']
   
    ordering_fields = ['product_name','created_at','id','category.id']

class ProductAdd(generics.ListCreateAPIView):
    
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()




    @method_decorator(cache_page(20))
    def get(self, *args, **kwargs):
        return super().get(*args, **kwargs)

class ProductUpdateDelete(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [AllowAny]
    
    serializer_class = ProductModelSerializer
    queryset = Product.objects.all()
    lookup_field = 'pk'




    # for Attribute,AtributeValue,ProductAttributes

class AttributeKeyList(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AttributeKeySerializer
    queryset = Attribute.objects.all()
    

class AttributeValueList(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = AttributeValueSerializer
    queryset = AttributeValue.objects.all()

class ProductAttributesList(generics.ListAPIView):
    # authentication_classes = [TokenAuthentication]
    permission_classes = [AllowAny]
    serializer_class = ProductAttributesSerializer
    queryset = ProductAttribute.objects.all()