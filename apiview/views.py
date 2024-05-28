from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, MusicKlip
from .serializers import CategorySerializer, MusicKlipSerializer


class CategoryAPI(APIView):
    def get(self, request):
        category = Category.objects.all()
        serializer = CategorySerializer(category, many=True)
        return Response(serializer.data)


class ProductSignsAPI(APIView):
    def get(self, request):
        product = MusicKlip.objects.all()
        serializer = MusicKlipSerializer(product, many=True)
        return Response(serializer.data)



class ProductDetailSignsAPI(APIView):
    def get(self, request, pk):
        product = MusicKlip.objects.get(pk=pk)
        serializer = MusicKlipSerializer(product)
        return Response(serializer.data)






class ProductSignsAPIDelete(APIView):
    def delete(self, request, pk):
        try:
            product = MusicKlip.objects.get(pk=pk)
            product.delete()
            serializer_data = {
                "signs": 'deleteed',
                "status": 'success',
                'status_code': 200
            }
        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": 'error',
                "status_code": 400
            }
        finally:
            return Response(serializer_data)
class ProductUpdate(APIView):
    def put(self, request, pk):
        try:
            product = MusicKlip.objects.get(pk=pk)
            serializer = MusicKlipSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "signs": 'updated',
                    "status": 'success',
                    "status_code": 200
                }

        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": 'error',
                "status_code": 400
            }
        finally:
            return Response(serializer_data)

    def patch(self,request,pk):
        try:
            product = MusicKlip.objects.get(pk=pk)
            serializer = MusicKlipSerializer(product,data=request.data,partial=True)
            if serializer.is_valid():
                serializer.save()
                serializer_data = {
                    "signs": 'updated',
                    "status": 'success',
                    "status_code": 200
                }

        except Exception as e:
            serializer_data = {
                "error": str(e),
                "status": 'error',
                "status_code": 400
            }
        finally:
            return Response(serializer_data)


