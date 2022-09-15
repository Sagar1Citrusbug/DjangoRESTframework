from rest_framework import generics, permissions, viewsets, mixins
from ..models import myUser
from .serializers import Userserializer


# class UserListView(viewsets.ModelViewSet):
#     queryset = myUser.objects.all()
#     serializer_class = Userserializer
#     permission_classes = [permissions.IsAuthenticated]


class apibymixin(mixins.ListModelMixin,mixins.CreateModelMixin,mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = myUser.objects.exclude(id__gt = 5)
    serializer_class =  Userserializer
    def get(self,request):
        return self.list(request)


class UserListView(generics.ListAPIView):
    queryset = myUser.objects.all()
    serializer_class = Userserializer
    # permission_classes = [permissions.IsAuthenticated]

class UserDetailView(generics.RetrieveAPIView):
    queryset= myUser.objects.all()
    serializer_class = Userserializer


from  rest_framework.authtoken.models import Token
for user in myUser.objects.all():

    Token.objects.get_or_create(user = user)

    