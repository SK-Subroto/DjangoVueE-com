from django.core.files.storage import FileSystemStorage
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import CategorySerializer, SupplierSerializer, ProductReadSerializer, ProductWriteSerializer
from .models import Category, Supplier, Product
from users.models import User, Token
import jwt
from django.db.models import Q


class CategoryView(APIView):

    def get(self, request):
        try:
            category = Category.objects.all()
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = CategorySerializer(category, many=True)
            return Response(serializer.data)


class CategoryCreate(APIView):

    def post(self, request):

        data = {}

        if request.method == "POST":
            serializer = CategorySerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_201_CREATED)

            data['error'] = "Failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CategoryUpdate(APIView):

    def put(self, request, pk):

        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "PUT":
            serializer = CategorySerializer(category, data=request.data)
            data = {}

            if serializer.is_valid():
                serializer.save()
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_201_CREATED)

            data['error'] = "Failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class CategoryDelete(APIView):

    def delete(self, request, pk):
        try:
            category = Category.objects.get(id=pk)
        except Category.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "DELETE":
            operation = category.delete()
            data = {}

            if operation:
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data['error'] = "Failed"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


#SUPPIERS
class SupplierView(APIView):

    def get(self, request):
        try:
            supplier = Supplier.objects.all()
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = SupplierSerializer(supplier, many=True)
            return Response(serializer.data)


class SupplierCreate(APIView):

    def post(self, request):

        if request.method == "POST":
            serializer = SupplierSerializer(data=request.data)

            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class SupplierUpdate(APIView):

    def put(self, request, pk):

        try:
            supplier = Supplier.objects.get(id=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "PUT":
            serializer = SupplierSerializer(supplier, data=request.data)
            data = {}

            if serializer.is_valid():
                serializer.save()
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_201_CREATED)

            data['error'] = "Failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class SupplierDelete(APIView):

    def delete(self, request, pk):
        try:
            supplier = Supplier.objects.get(id=pk)
        except Supplier.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "DELETE":
            operation = supplier.delete()
            data = {}

            if operation:
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data['error'] = "Failed"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)



#PRODUCT
class ProductView(APIView):

    def get(self, request):
        try:
            product = Product.objects.all()
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = ProductReadSerializer(product, many=True)
            return Response(serializer.data)


class ProductCreate(APIView):

    def post(self, request):

        print(request.data)

        # category = Category.objects.get(pk=1)
        # supplier = Supplier.objects.get(pk=1)
        image = request.data['image'].split('/')[2]

        # product = Product(category=category, supplier=supplier)
        product = Product(img=image)
        data = {}
        if request.method == "POST":
            serializer = ProductWriteSerializer(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                data['message'] = "success"
                return Response(data=data, status=status.HTTP_201_CREATED)
            data['message'] = "failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


# class ProductImgUpload(APIView):
#
#     def post(self, request):
#         print(request.data)
#         data = {}
#         if request.method == "POST":
#             serializer = ProductImageSerializer(data=request.data)
#
#             if serializer.is_valid():
#                 serializer.save()
#                 data['uploadedUrl'] = serializer.data["img"]
#                 # data['message'] = "sucess"
#                 return Response(data=data, status=status.HTTP_201_CREATED)
#
#             data['message'] = "failed"
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductUpdate(APIView):

    def put(self, request, pk):

        print(request.data)

        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        # category = Category.objects.get(pk=request.data['category'])
        # supplier = Supplier.objects.get(pk=request.data['supplier'])
        # image = request.data['img'].split('/')[2]

        # product = Product(img=image)
        print(product)
        data = {}
        if request.method == "PUT":
            serializer = ProductWriteSerializer(product, data=request.data)

            if serializer.is_valid():
                serializer.save()
                data['message'] = "success"
                return Response(data=data, status=status.HTTP_201_CREATED)
            data['message'] = "failed"
            return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ProductDelete(APIView):

    def delete(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "DELETE":
            operation = product.delete()
            data = {}

            if operation:
                data['message'] = "Success"
                return Response(data=data, status=status.HTTP_200_OK)
            else:
                data['error'] = "Failed"
                return Response(data=data, status=status.HTTP_400_BAD_REQUEST)


class ProductSingleView(APIView):

    def get(self, request, pk):
        try:
            product = Product.objects.get(id=pk)
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        if request.method == "GET":
            serializer = ProductReadSerializer(product)
            return Response(serializer.data)


@api_view(['POST'])
def simple_upload(request):
    data = {}
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        # uploaded_file_url = fs.url(filename)
        data['uploadedUrl'] = fs.url(filename)
    return Response(data=data, status=status.HTTP_201_CREATED)