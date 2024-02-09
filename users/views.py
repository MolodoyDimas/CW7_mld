from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework import viewsets, status
from users.models import User
from users.serializers import UserSerializer
from requests import Response

class UserViewSet(viewsets.ModelViewSet):
    """
    Набор представлений для пользовательской модели.
    """

    allowe_http_methods = ["post"] #подсказка
    permisson_class = [AllowAny] #подсказка

    def create(self, request):


        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)

        password = serializer.data["password"]
        user = User.objects.get(pk=serializer.data["id"])
        user.set_password(password)
        user.save()

        return Response(
            serializer.data,
            status=status.HTTP_201_CREATED,
            headers=headers
        )

    #queryset = User.objects.all()
    #serializer_class = UserSerializer
    #permission_classes = [AllowAny]
