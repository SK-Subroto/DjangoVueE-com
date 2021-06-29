from django.urls import path
from .views import (CategoryView,
                    CategoryCreate,
                    CategoryUpdate,
                    CategoryDelete,
                    SupplierView,
                    SupplierCreate,
                    SupplierUpdate,
                    SupplierDelete,
                    ProductView,
                    ProductSingleView,
                    ProductCreate,
                    ProductUpdate,
                    ProductDelete,
                    simple_upload)

urlpatterns = [
    path('category', CategoryView.as_view()),
    path('category/create', CategoryCreate.as_view()),
    path('category/update/<str:pk>', CategoryUpdate.as_view()),
    path('category/delete/<str:pk>', CategoryDelete.as_view()),

    path('supplier', SupplierView.as_view()),
    path('supplier/create', SupplierCreate.as_view()),
    path('supplier/update/<str:pk>', SupplierUpdate.as_view()),
    path('supplier/delete/<str:pk>', SupplierDelete.as_view()),

    path('product', ProductView.as_view()),
    path('product/view/<str:pk>', ProductSingleView.as_view()),
    path('product/create', ProductCreate.as_view()),
    path('product/update/<str:pk>', ProductUpdate.as_view()),
    path('product/delete/<str:pk>', ProductDelete.as_view()),
    path('product/upload_file', simple_upload),
]