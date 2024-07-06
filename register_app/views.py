from rest_framework import viewsets
from .models import UserInformation, RegionUser, ClassUser
from .serializers import UserSerializer, RegionSerializer, ClassSerializer, UserGetSerializer
from django.core.mail import send_mail
import asyncio
import aiohttp
from telegram import Bot
from django.conf import settings


class RegionViewSet(viewsets.ModelViewSet):
    queryset = RegionUser.objects.all()
    serializer_class = RegionSerializer


class ClassViewSet(viewsets.ModelViewSet):
    queryset = ClassUser.objects.all()
    serializer_class = ClassSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = UserInformation.objects.all()

    def get_serializer_class(self):
        if self.request.method == "GET":
            return UserGetSerializer
        return UserSerializer


    def perform_create(self, serializer):
        instance = serializer.save()
        self.send_notification_email(instance)
        asyncio.run(self.send_notification_telegram(instance))

    def send_notification_email(self, instance):
        subject = f'New Author Information Submitted by {instance.first_name}'
        message = f'''
        A new user information entry has been submitted.

        Your Details:
        Name: {instance.first_name} 
        Class: {instance.class_user}   
        Region: {instance.region}
        Phone: {instance.phone_your}
        '''
        admin_email = 'alijonovasilbek058@gmail.com'
        send_mail(subject, message, 'no-reply@example.com', [admin_email])

    async def send_notification_telegram(self, instance):
        try:
            bot = Bot(token=settings.TELEGRAM_BOT_TOKEN, base_url="https://api.telegram.org/bot")
            chat_id = settings.TELEGRAM_CHAT_ID
            message = f'''
            Yangi Registratsiya Xati:
            Name: {instance.first_name}
            Class: {instance.class_user}
            Region: {instance.region}
            Phone: {instance.phone_your}
            '''
            await bot.send_message(chat_id=chat_id, text=message)
        except Exception as e:
            print(f"Error sending Telegram message: {e}")
