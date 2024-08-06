from django.urls import path,include
from texnomart import views
from texnomart import auth

urlpatterns = [
    # Category section
    path('categories/',views.CategoryList.as_view(),name = 'category-list'),
    path('category/<slug:slug>/',views.CategoryDetail.as_view(), name = 'category_detail'),
    path('category/category-add/',views.CategoryListCreate.as_view(),name = 'category-add'),
    path('category/<slug:slug>/delete/',views.CategoryDelete.as_view(),name = 'category_delete'),
    path('category/<slug:slug>/edit/',views.CategoryChange.as_view(),name = 'category_update'),
    path('product-add/',views.ProductAdd.as_view(),name = 'product-add'),

    # Product section
     path('',views.ProductList.as_view(),name = 'product-list'),
     path('product/detail/<int:pk>/',views.ProductUpdateDelete.as_view(),name = 'update_delete'),

    #  Attributekey,AttributeValue,ProductAttributes
    path('attribute-key/',views.AttributeKeyList.as_view(),name = 'attribute-key'),
    path('attribute-value/',views.AttributeValueList.as_view(),name = 'attribute-value'),
    path('product-attributes/',views.ProductAttributesList.as_view(),name = 'product-attributes'),
    

   # Login Register Logout

    path("login/", auth.UserLoginAPIView.as_view(), name="user_login"),
    path("register/", auth.RegisterUserAPI.as_view(), name="user_register"),
    path("logout/", auth.UserLogoutAPIView.as_view(), name="user_logout")
    
]