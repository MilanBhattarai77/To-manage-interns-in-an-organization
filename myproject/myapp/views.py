from django.shortcuts import get_object_or_404
from .serializers import UserProfileSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from .models import UserProfile

class UserViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
     
    def create(self, request):
        queryset = UserProfile.objects.all()
        serializer = UserProfileSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def update(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
     

    def partial_update(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
     

    def destroy(self, request, pk=None):
        queryset = UserProfile.objects.all()
        user = get_object_or_404(queryset, pk=pk)
        serializer = UserProfileSerializer(user)
        return Response(serializer.data)
     

