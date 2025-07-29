from modeltranslation.translator import translator, TranslationOptions
from .models import Msg

class MsgTranslationOptions(TranslationOptions):
    fields = ('messagehead', 'message')
    required_languages = ('en', 'ar')

translator.register(Msg, MsgTranslationOptions)