from app.serializers import CustomUserSerializer
from app.models import CustomUser
from rest_framework.views import APIView
from rest_framework.response import Response


class CustomUserView(APIView):
    def get(self, request):
        queryset = CustomUser.objects.all()
        serializer = CustomUserSerializer(queryset, many=True)
        return Response(data=serializer.data)
