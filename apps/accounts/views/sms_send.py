from apps.accounts.serializers import RegisterSerializer 
from rest_framework.generics import GenericAPIView
from apps.common.utils import send_sms, generate_code
from rest_framework.response import Response
from rest_framework import status


class SendSmsAPIView(GenericAPIView):
    serializer_class = RegisterSerializer
    
    def post(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        code = generate_code()
        result = send_sms(phone=serializer.validated_data["phone"], message=f"UICdev platformasiga kirish uchun kod: {code}")
        return Response(result, status=status.HTTP_200_OK)


# class VerifySmsAPIView(GenericAPIView):
#     serializer_class = RegisterSerializer
    
#     def post(self, request):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)

#         return Response(serializer.validated_data, status=status.HTTP_200_OK)