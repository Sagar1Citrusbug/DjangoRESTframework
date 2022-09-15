from dataclasses import field
from email.policy import default
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from ..models import myUser



class  Userserializer(serializers.ModelSerializer):
    class Meta:
        model = myUser
        fields = ['name','email']

# class  Userserializer(serializers.Serializer):
#     id = serializers.IntegerField(read_only  = True)
#     name = serializers.CharField(max_length = 35)
#     email = serializers.EmailField(default="sagar1.citrusbug@gmail.com")
    
#     def create(self, validated_data):
#         return myUser.objects.create(**validated_data)

#     def update(self, instance, validated_data):
#         instance.name = validated_data.get('name', instance.name)
#         instance.email = validated_data.get('email',instance.email)
#         instance.save()
#         return instance
