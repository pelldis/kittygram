from rest_framework.views import APIView
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Cat
from .serializers import CatSerializer


class APICat(APIView):
    def get(self, request):
        cats = Cat.objects.all()
        serializer = CatSerializer(cats, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CatSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class APICatDetail(APIView):
    def get(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat)
        return Response(serializer.data, status.HTTP_200_OK)

    def put(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_204_NO_CONTENT)

    def patch(self, request, pk):
        cat = Cat.objects.get(id=pk)
        serializer = CatSerializer(cat, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status.HTTP_200_OK)
        return Response(serializer.errors, status.HTTP_204_NO_CONTENT)

    def delete(self, request, pk):
        try:
            cat = Cat.objects.get(id=pk)
            cat.delete()
            return Response('', status.HTTP_204_NO_CONTENT)
        except Exception as error:
            return Response(f'{error}', status.HTTP_404_NOT_FOUND)
