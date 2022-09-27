
from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from ..models import myUser, book, Author, transaction


class  Userserializer(serializers.ModelSerializer):
    book_count = serializers.SerializerMethodField()

    class Meta:
        model = myUser
        fields = ['name','email', 'book_count']
    def get_book_count(self,obj):
        return obj.user_has_books.count()
class Authorserializer(serializers.ModelSerializer):
 
    class Meta:
        model = Author
        fields = ['name','email']

class bs(serializers.ModelSerializer):
    
    author = serializers.SlugRelatedField(queryset = Author.objects.all(), slug_field='name')
   
  

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
        fields = ['title','author', 'user' ]
from math import ceil
from datetime import datetime, timedelta
from pytz import timezone
class ts(serializers.ModelSerializer):
    books  =serializers.SlugRelatedField(queryset = book.objects.all(),slug_field='title',many = False)
    user  = serializers.SlugRelatedField(queryset  = myUser.objects.all(),slug_field='email', many = False)

    Issue_Date = serializers.SerializerMethodField()
    Return_Date = serializers.SerializerMethodField()
    price  = serializers.SerializerMethodField()
    Issued_Time = serializers.SerializerMethodField()
    Return_time = serializers.SerializerMethodField()


    # def create(self, validated_data):
    #     return transaction.objects.create(**validated_data)

    class Meta:
        model  = transaction
        # fields = '__all__'
        fields = ['user','books', 'Issue_Date', 'Return_Date','Issued_Time', 'Return_time' , 'price' ]
    
    

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
    
    def get_Issued_Time(self, obj):
        
        now = timezone('Asia/Kolkata')
        time = datetime.now().astimezone(now) - obj.issue_date
        return f"{time.days} days {time.seconds//3600} hours { (time.seconds - (time.seconds//3600)*3600)//60 } Minutes ago"


    def get_Return_time(self, obj):
        now = timezone('Asia/Kolkata')
        time = obj.return_date+timedelta(hours = datetime.now().hour, minutes = datetime.now().minute, seconds= datetime.now().second+1) - datetime.now().astimezone(now)
        return f"{time.days} days {time.seconds//3600} hours { (time.seconds - (time.seconds//3600)*3600)//60 } Minutes after"


class PostTransactionserializer(serializers.ModelSerializer):
    books  =serializers.PrimaryKeyRelatedField(queryset = book.objects.all(),many = False)
    user  = serializers.PrimaryKeyRelatedField(queryset  = myUser.objects.all(), many = False)


    class Meta:
        model = transaction
        fields =['books', 'user', 'return_date']
       
    def validate_return_date(self, data):
        data = data + timedelta(hours = datetime.now().hour, minutes = datetime.now().minute, seconds= datetime.now().second+1)
        if  data < datetime.now().astimezone(timezone('Asia/Kolkata')):
            raise serializers.ValidationError({'return_date':'return date inappropriate'})
        return data 