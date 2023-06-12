from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import serializers
from myapp.models import RecipeDetail,Category_Tag, TagList
#from myapp.serializers import RecipeSerializer
from django.contrib.auth.models import User
# from django.core.validators import FileExtensionValidator, FileSizeValidator
# from django.core.files.images import get_image_dimensions
# from django.conf import settings
# from django.core.exceptions import ValidationError
# from django.utils.deconstruct import deconstructible
from django.contrib.auth import get_user_model

User = get_user_model()

class CategoryTagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Category_Tag
        fields = '__all__'

class TagListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TagList
        fields = '__all__'


class RecipeSerializer(serializers.ModelSerializer):
    category = CategoryTagSerializer(many=True, read_only= True)

    class Meta:
        model = RecipeDetail
        fields = '__all__'

    # def create(self, validated_data):
    #     category_data = validated_data.pop('category')
    #     recipe = RecipeDetail.objects.create(**validated_data)
    #
    #     for category_item in category_data:
    #         Category_Tag.objects.create(recipe=recipe, name=category_item['name'])
    #
    #     return recipe


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'email']

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        user.save()
        return user

# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(validated_data['username'], validated_data['email'], validated_data['password'])
        return user


