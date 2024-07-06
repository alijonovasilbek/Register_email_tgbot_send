from rest_framework import serializers
from .models import UserInformation,RegionUser,ClassUser
from rest_framework.fields import SerializerMethodField


class RegionSerializer(serializers.ModelSerializer):
    class Meta:
        model=RegionUser
        fields='__all__'


class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model=ClassUser
        fields='__all__'


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = '__all__'




class UserGetSerializer(serializers.ModelSerializer):
    region_user=SerializerMethodField(method_name='get_region',read_only=True)
    class_user=SerializerMethodField(method_name='get_class',read_only=True)

    class Meta:
        model=UserInformation
        fields='__all__'

    def get_region(self,obj):
        return obj.region.region_name

    def get_class(self,obj):
        return obj.class_user.class_name



