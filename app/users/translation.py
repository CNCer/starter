
from modeltranslation.translator import translator, TranslationOptions
from .models import User

class UserTranslationOptions(TranslationOptions):
    fields = ('first_name', 'last_name')
    #required_languages = ('en', 'ar')

translator.register(User, UserTranslationOptions)


"""
Model Forms:
To show only one traslation

from news.models import News
from modeltranslation.forms import TranslationModelForm

class MyForm(TranslationModelForm):
    class Meta:
        model = News

"""