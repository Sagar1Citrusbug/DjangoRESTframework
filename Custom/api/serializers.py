
from rest_framework import serializers
from ..models import myUser, book, Author, transaction



class  Userserializer(serializers.ModelSerializer):
    user_has_books = serializers.PrimaryKeyRelatedField(many = True, read_only = True)
    
    class Meta:
        model = myUser
        fields = ['name','email', 'user_has_books']

class Authorserializer(serializers.ModelSerializer):
    author_books = serializers.StringRelatedField(many = True)

    class Meta:
        model = Author
        fields = ['name','author_books']

class bs(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(queryset = Author.objects.all(), slug_field='name')
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
class ts(serializers.ModelSerializer):
    books  =serializers.SlugRelatedField(read_only =  True, slug_field= 'title', many = False)
    user  = serializers.SlugRelatedField(read_only = True, slug_field='name', many = False)

    class Meta:
        model  = transaction
        fields = ['user','books', 'issue_date', 'return_date', 'price' ]
