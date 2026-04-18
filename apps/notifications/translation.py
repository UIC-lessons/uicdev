from modeltranslation.translator import register, TranslationOptions
from .models import Notification


@register(Notification)
class NotificationTranslation(TranslationOptions):
    fields = ("title", "message", "course", "module", "category")

