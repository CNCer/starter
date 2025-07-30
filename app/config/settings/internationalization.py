import os
from django.utils.translation import gettext_lazy as _
from .base import APP_DIR

LANGUAGE_CODE = 'en'

TIME_ZONE = 'Africa/Cairo'

USE_I18N = True

USE_TZ = True

LANGUAGES  = (
    ('en', 'English'),
    ('ar', 'عربى'),
)

MODELTRANSLATION_DEFAULT_LANGUAGE = 'en'


LANGUAGE_COOKIE_AGE = 1209600
LANGUAGE_COOKIE_NAME = 'lang_cookie'
THEME_COOKIE_NAME = 'theme_cookie'

LOCALE_PATHS = (
    os.path.join(APP_DIR, 'locale/'),
)

THEMES  = (
    ('silk', _('silk')),
    ('abyss', _('abyss')),
    ('caramellatte', _('caramel latte')),
    ('sunset', _('sunset')),
    ('nord', _('nord')),
    ('dim', _('dim')),
    ('winter', _('winter')),
    ('coffee', _('coffee')),
    ('night', _('night')),
    ('lemonade', _('lemonade')),
    ('acid', _('acid')),
    ('business', _('business')),
    ('autumn', _('autumn')),
    ('cmyk', _('cmyk')),
    ('dracula', _('dracula')),
    ('luxury', _('luxury')),
    ('black', _('black')),
    ('wireframe', _('wireframe')),
    ('fantasy', _('fantasy')),
    ('pastel', _('pastel')),
    ('lofi', _('lofi')),
    ('aqua', _('aqua')),
    ('forest', _('forest')),
    ('garden', _('garden')),
    ('halloween', _('halloween')),
    ('valentine', _('valentine')),
    ('cyberpunk', _('cyberpunk')),
    ('retro', _('retro')),
    ('synthwave', _('synthwave')),
    ('corporate', _('corporate')),
    ('emerald', _('emerald')),
    ('bumblebee', _('bumblebee')),
    ('cupcake', _('cupcake')),
    ('dark', _('dark')),
    ('light', _('light')),
    
)