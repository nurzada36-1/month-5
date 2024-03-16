import random

from django.core.mail import send_mail
from rest_framework import status
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate, login
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from Afisha import settings
from .models import UserConfirmation
from .serializers import UserRegisterSerializer, UserLoginSerializer, UserConfirmationSerializer


@api_view(['POST'])
def registration_api_view(request):
    if request.method == 'POST':
        serializer = UserRegisterSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()

        code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        confirmation = UserConfirmation.objects.create(user=user, code=code)
        confirmation.save()

        subject = 'Code'
        message = f'Your code: {code}'
        sender = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, sender, recipient_list)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
def confirm_user_api_view(request):
    serializer = UserConfirmationSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    code = serializer.validated_data.get('code')

    try:
        confirmation = UserConfirmation.objects.get(code=code)
    except UserConfirmation.DoesNotExist:
        return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_404_NOT_FOUND)

    user = confirmation.user
    user.is_active = True
    user.save()
    confirmation.delete()

    return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


@api_view(['POST'])
def login_api_view(request):
    serializer = UserLoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = authenticate(**serializer.validated_data)
    if user:
        login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        user.save()
        return Response({'token': token.key})
    return Response({'error': 'Invalid credentials'}, status=400)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def logout(request):
    try:
        token = Token.objects.get(user=request.user)
        token.delete()
        return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
    except Token.DoesNotExist:
        return Response({'message': 'User is already logged out'}, status=status.HTTP_200_OK)


class RegistrationAPIView(APIView):
    serializer_class = UserRegisterSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        code = ''.join([str(random.randint(0, 9)) for _ in range(5)])
        confirmation = UserConfirmation.objects.create(user=user, code=code)
        confirmation.save()

        subject = 'Your code'
        message = f'Your code: {code}'
        sender = settings.EMAIL_HOST_USER
        recipient_list = [user.email]
        send_mail(subject, message, sender, recipient_list)

        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ConfirmUserAPIView(APIView):
    serializer_class = UserConfirmationSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = serializer.validated_data.get('code')

        try:
            confirmation = UserConfirmation.objects.get(code=code)
        except UserConfirmation.DoesNotExist:
            return Response({'error': 'Invalid confirmation code'}, status=status.HTTP_404_NOT_FOUND)

        user = confirmation.user
        user.is_active = True
        user.save()
        confirmation.delete()

        return Response({'status': 'User activated'}, status=status.HTTP_200_OK)


class LoginAPIView(APIView):
    serializer_class = UserLoginSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = authenticate(**serializer.validated_data)
        if user:
            login(request, user)
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        return Response({'error': 'Invalid credentials'}, status=status.HTTP_400_BAD_REQUEST)


class LogoutAPIView(APIView):
    permission_classes = (IsAuthenticated,)

    def post(self, request):
        try:
            token = Token.objects.get(user=request.user)
            token.delete()
            return Response({'message': 'User logged out'}, status=status.HTTP_200_OK)
        except Token.DoesNotExist:
            return Response({'message': 'User is already logged out'}, status=status.HTTP_200_OK)
