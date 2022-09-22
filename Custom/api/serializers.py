
from rest_framework import serializers
from ..models import myUser, book, Author, transaction


class  Userserializer(serializers.ModelSerializer):
     
    class Meta:
        model = myUser
        fields = ['name','email', 'book_count']

class Authorserializer(serializers.ModelSerializer):
 
    class Meta:
        model = Author
        fields = ['name','email']

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
from math import ceil
from datetime import datetime
from pytz import timezone
class ts(serializers.ModelSerializer):
    books  =serializers.SlugRelatedField(read_only =  True, slug_field= 'title', many = False)
    user  = serializers.SlugRelatedField(read_only = True, slug_field='name', many = False)
    Issue_Date = serializers.SerializerMethodField()
    Return_Date = serializers.SerializerMethodField()
    price  = serializers.SerializerMethodField()
    Time = serializers.SerializerMethodField()
    class Meta:
        model  = transaction
        fields = ['user','books', 'Issue_Date', 'Return_Date','Time' , 'price' ]


    def get_price(self, obj):
       if (obj.return_date - obj.issue_date).days == 0:
        book_price = 10
        return book_price
       else:
            book_price = ceil((obj.return_date - obj.issue_date).days) * 10
            return book_price        

    def get_Issue_Date(self, obj):
        return datetime.strftime(obj.issue_date, '%d/%m/%y')

    def get_Return_Date(self, obj):
        return datetime.strftime(obj.return_date, '%d/%m/%y')
    
    def get_Time(self, obj):
        
        now = timezone('Asia/Kolkata')
        time = datetime.now().astimezone(now) - obj.issue_date
        return f"{time.days} days {time.seconds//3600} hours { (time.seconds - (time.seconds//3600)*3600)//60 } Minutes ago"

    