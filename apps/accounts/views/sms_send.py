from django.db import transaction
from django.core.cache import cache
from rest_framework.exceptions import ValidationError
from apps.accounts.serializers import RegisterSerializer, VerifySerializer, UserProfileSerializer
from rest_framework.generics import GenericAPIView
from apps.common.utils import send_sms, generate_code
from rest_framework.response import Response
from rest_framework import status
from apps.accounts.models import User
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.authentication import SessionAuthentication


class SendSmsAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=True)
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        phone = serializer.validated_data["phone"]
        password = serializer.validated_data["password"]
        
        with transaction.atomic():
            user = User.objects.select_for_update().filter(phone=phone).first()

            if user and user.is_active:
                raise ValidationError("User already exists and is active")

            if user is None:
                user = serializer.save()
            else:
                user.set_password(password)
                user.is_active = False
                user.save(update_fields=["password", "is_active"])

        valid_phone = user.phone.replace("+", "")
        code = generate_code()
        result = send_sms(phone=valid_phone, message=f"UICdev platformasiga kirish uchun kod: {code}", from_name="UICdev")
        cache.set(f"sms_kod:{user.phone}", code, timeout=60*3)
        return Response(result, status=status.HTTP_200_OK)



class VerifySmsAPIView(GenericAPIView):
    serializer_class = VerifySerializer
    permission_classes = [AllowAny]
    

    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        phone = serializer.validated_data["phone"]
        code = serializer.validated_data["code"]
        user = User.objects.filter(phone=phone).first()
        valid_phone = user.phone.replace("+", "")

        cached_kod = cache.get(f"sms_kod:{valid_phone}")

        if not user:
            raise ValidationError("User not found")
        if cached_kod is None:
            raise ValidationError("Kod vaqti tugadi, qayta urining")
        if cached_kod != code:
            raise ValidationError("Kod noto'g'ri")
        
        with transaction.atomic():
            user.is_active = True
            user.save(update_fields=["is_active"])
            cache.delete(f"sms_kod:{phone}")

        return Response({"message": "User verified successfully"}, status=status.HTTP_200_OK)


class UserProfileAPIView(GenericAPIView):
    queryset = User.objects.filter(is_active=True).select_related("avatar")
    serializer_class = UserProfileSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [SessionAuthentication]

    def get_object(self):
        return self.request.user
