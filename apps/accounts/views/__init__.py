from .user import UserListCreateAPIView, UserRetrieveUpdateDestroyAPIView
from .education import EducationListCreateAPIView, EducationRetrieveUpdateDestroyAPIView
from .user_certificate import (
    UserCertificateListCreateAPIView,
    UserCertificateRetrieveUpdateDestroyAPIView,
)
from .user_education import (
    UserEducationListCreateAPIView,
    UserEducationRetrieveUpdateDestroyAPIView,
)
from .user_experience import (
    UserExperienceListCreateAPIView,
    UserExperienceRetrieveUpdateDestroyAPIView,
)
from .sms_send import SendSmsAPIView
__all__ = [
    "UserListCreateAPIView",
    "UserRetrieveUpdateDestroyAPIView",
    "EducationListCreateAPIView",
    "EducationRetrieveUpdateDestroyAPIView",
    "UserCertificateListCreateAPIView",
    "UserCertificateRetrieveUpdateDestroyAPIView",
    "UserEducationListCreateAPIView",
    "UserEducationRetrieveUpdateDestroyAPIView",
    "UserExperienceListCreateAPIView",
    "UserExperienceRetrieveUpdateDestroyAPIView",
    "SendSmsAPIView",
]
