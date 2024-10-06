from rest_framework import serializers
from .models import User, Family, Member, Church, Emirate, SubArea, FatherConf, ProfessionCategory


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'email', 'phone_number', 'password']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            email=validated_data['email'],
            password=validated_data['password'],
            phone_number=validated_data.get('phone_number', None),
        )
        return user


# Family Serializer
class FamilySerializer(serializers.ModelSerializer):
    class Meta:
        model = Family
        fields = '__all__'


# Member Serializer
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = '__all__'


# Lookup Serializers
class ChurchSerializer(serializers.ModelSerializer):
    class Meta:
        model = Church
        fields = '__all__'


class EmirateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Emirate
        fields = '__all__'


class SubAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = SubArea
        fields = '__all__'


class FatherConfSerializer(serializers.ModelSerializer):
    class Meta:
        model = FatherConf
        fields = '__all__'


class ProfessionCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProfessionCategory
        fields = '__all__'
