from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import filters
from rest_framework import status
from .serializers import *

class UserAuthentication(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response(token.key)

class RouterList(APIView):

    def get(self, request):
        model = routerapi.objects.filter(is_delete=0)
        serializer = RouterSrtislizer(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = RouterSrtislizer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RouterFilter(APIView):
    def get_routerFilter(self, loopback):
        try:
            model = routerapi.objects.filter( loopback__startswith  = loopback, is_delete=0)
            print(model)
            return model
        except routerapi.DoesNotExist:
            return

    def get(self, request, loopback):
        if not self.get_routerFilter(loopback):
            return Response(f'Router with {loopback} is not in database....', status=status.HTTP_404_NOT_FOUND)

        serializer = RouterSrtislizer(self.get_routerFilter(loopback))
        print(serializer.data)
        return Response(serializer.data)

class RouterDetail(APIView):
    def get_router(self, routerid):
        try:
            model = routerapi.objects.get(id=routerid,is_delete=0)
            return model
        except routerapi.DoesNotExist:
            return

    def get(self, request, routerid):
        if not self.get_router(routerid):
            return Response(f'Router with {routerid} is not in database', status=status.HTTP_404_NOT_FOUND)

        serializer = RouterSrtislizer(self.get_router(routerid))
        return Response(serializer.data)

        serializer = RouterSrtislizer(self.get_router(routerid), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, routerid):

        if not self.get_router(routerid):
            return Response(f'Router with {routerid} is not in database', status=status.HTTP_404_NOT_FOUND)

        deleteset = {"is_delete": "1"}
        serializer = RouterSrtislizer(self.get_router(routerid), data=deleteset)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_204_NO_CONTENT)
