from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import api_view
from django.core.mail import send_mail

from config.settings import EMAIL_HOST_USER
from .models import FAQ, Requirements, UserInfo
from .serializers import (
    FAQSerializer, FAQGetSerializer,
    RequirementsSerializer, RequirementsGetSerializer,
    UserInfoSerializer
)


class FAQViewSet(ModelViewSet):
    queryset = FAQ.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return FAQGetSerializer
        return FAQSerializer


class RequirementsViewSet(ModelViewSet):
    queryset = Requirements.objects.all()
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.request.method == 'GET':
            return RequirementsGetSerializer
        return RequirementsSerializer


@api_view(['POST'])
def send_email(request):
    if request.method == 'POST':
        serializer = UserInfoSerializer(data=request.data)
        if serializer.is_valid():
            try:
                send_mail(
                    subject=serializer.validated_data['subject'],
                    message=serializer.validated_data['message'],
                    from_email=EMAIL_HOST_USER,
                    recipient_list=[serializer.validated_data['email']],
                )
                user_info = UserInfo(
                    email=serializer.validated_data['email'],
                    user_name=serializer.validated_data['name'],
                    message=serializer.validated_data['message']
                )
                user_info.save()
                return Response(
                    {'message': 'Email is sent successfully'},
                    status=status.HTTP_200_OK
                )
            except Exception as e:
                return Response(
                    {'message': f'Failed to send email: {str(e)}'},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )
        else:
            return Response(
                {'message': 'Invalid data', 'errors': serializer.errors},
                status=status.HTTP_400_BAD_REQUEST
            )
    return Response(
        {'message': 'Method not allowed'},
        status=status.HTTP_405_METHOD_NOT_ALLOWED
    )


