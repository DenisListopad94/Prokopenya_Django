from django.http import Http404
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import serializers, status, mixins, generics
from django.contrib.auth.models import User
from .serializers import UserSerializer, HotelOwnerSerializer, HobbiesModelSerializer
from booking_app.models import HotelOwner, Hobby


# Create your views here.

class UserApiView(APIView):

    def get(self, request, format=None):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data)


class HotelOwnerListView(APIView):

    def get(self, request, format=None):
        hotel_owners = HotelOwner.objects.all()
        serializer = HotelOwnerSerializer(hotel_owners, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = HotelOwnerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HotelOwnerDetailView(APIView):

    def get_object(self, pk):
        try:
            return HotelOwner.objects.get(pk=pk)
        except HotelOwner.DoesNotExist:
            raise Http404

    def get(self, request, pk):  # Обратите внимание на этот метод
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner)
        return Response(serializer.data)

    def put(self, request, pk):
        owner = self.get_object(pk)
        serializer = HotelOwnerSerializer(owner, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        owner = self.get_object(pk)
        owner.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class HobbyListApiView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Hobby.objects.all()
    serializer_class = HobbiesModelSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
