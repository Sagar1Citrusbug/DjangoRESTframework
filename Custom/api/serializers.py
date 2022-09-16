from dataclasses import field
from email.policy import default
from unittest.util import _MAX_LENGTH
from rest_framework import serializers
from ..models import myUser, book, Author



class  Userserializer(serializers.ModelSerializer):
    user_has_books = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    
    class Meta:
        model = myUser
        fields = ['name','email', 'user_has_books']

class Authorserializer(serializers.ModelSerializer):
    author_books = serializers.StringRelatedField(many = True)

    class Meta:
        model = Author
        fields = "__all__"

class bs(serializers.ModelSerializer):
    

    class Meta:
        model = book
        fields = '__all__'

class bookuser(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset = Author.objects.all(),slug_field='name', many = False )
    user = serializers.StringRelatedField(many = False)

    def __str__(self):
        return self.author.name
    class Meta:
        model = book
        fields = ['title','author', 'user'  ]


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
