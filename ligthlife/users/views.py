from rest_framework.generics import ListAPIView
from users.models import Profile
from users.serializers import UserSerializer


class UserAPIView(ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
