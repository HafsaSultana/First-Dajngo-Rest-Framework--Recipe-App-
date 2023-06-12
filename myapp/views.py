from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

from django.http import Http404
from rest_framework.views import APIView

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from django.contrib.auth.models import User
from rest_framework import mixins
from rest_framework import generics, permissions
from django.db import transaction

from django.contrib.auth import login
from rest_framework.authtoken.serializers import AuthTokenSerializer
from knox.views import LoginView as KnoxLoginView

from rest_framework import serializers
from myapp.models import RecipeDetail, TagList
from myapp.serializers import RecipeSerializer, TagListSerializer
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser

from knox.models import AuthToken
from .serializers import UserSerializer, RegisterSerializer
from rest_framework.permissions import IsAuthenticated

from rest_framework.authentication import TokenAuthentication, SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.authtoken.models import Token


# Register API
class UserRegister(APIView):

    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            user = User.objects.get(username = serializer.data['username'])
            token, created = Token.objects.get_or_create(user=user)
            return Response({
            'status': status.HTTP_201_CREATED,
            'token': str(token.key),
            'payload':serializer.data,
        })
        return Response({'error':serializer.errors,'status': status.HTTP_201_CREATED, })

class UserLogin(APIView):

    def post(self, request, format=None):
        serializer = AuthTokenSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            if created:
                response_data = {
                    'message': 'Successfully Login',
                    'token': token.key,
                    'status': status.HTTP_201_CREATED }
            else:
                response_data = {
                    'message': 'Successfully Login',
                    'token': token.key,
                    'status': status.HTTP_200_OK}
            return Response(response_data)
        return Response({'error': serializer.errors, 'status': status.HTTP_400_BAD_REQUEST})



class RecipeList(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, format=None):
        recipe = RecipeDetail.objects.all()
        serializer = RecipeSerializer(recipe, many=True)
        data = serializer.data

        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = RecipeSerializer(data=request.data)
        if serializer.is_valid():
            user = request.user  # Get the current user
            instance = serializer.save(user=user)
            tags = request.data.get("tags").split(',')

            tag_list = []
            for tag in tags:
                tag_list.append(TagList(hash_tag=tag, user=user, recipe=instance))
            TagList.objects.bulk_create(tag_list)

            response_data = {
                "tags": tags,
                "data": serializer.data
            }
            return Response(response_data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class Details_Recipe(APIView):
    # Token Authentication
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_object(self, pk):
        try:
            return RecipeDetail.objects.get(pk=pk)
        except RecipeDetail.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        recipe = self.get_object(pk)
        serializer = RecipeSerializer(recipe, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        recipe = self.get_object(pk)
        recipe.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)














class Family(APIView):

    def post(self, request,format=None):
        #a = ['hafsa','foysal','sajid','fahima','masuma','fahim']
        x = request.data.get('x')
        y = request.data.get('y')
        q = request.data.get('q')
        z = int(x)+int(y)+int(q)
        return Response({'z':z})

    def get(self, request):
        z=0
        if 'z' in request.GET:
            z = int(request.GET.get('z'))
        return Response({'z': z})


