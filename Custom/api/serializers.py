
from rest_framework import serializers
from ..models import myUser, book, Author, transaction


class  Userserializer(serializers.ModelSerializer):
     
    class Meta:
        model = myUser
        fields = ['name','email', 'book_count']

class Authorserializer(serializers.ModelSerializer):
 
    class Meta:
        model = Author
        fields = ['name']

class bs(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(queryset = Author.objects.all(), slug_field='name')
    user = serializers.StringRelatedField(many = False)
    class Meta:
        model = book
        fields ='__all__' 

class bookuser(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(queryset = Author.objects.all(),slug_field='name', many = True )
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
        fields = ['user','books', 'Issue_Date', 'Return_Date','Time' , 'price' ]
