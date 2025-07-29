from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image



# Create your models here.
class User(AbstractUser):

    class Meta:
        
        verbose_name = _("User")
        verbose_name_plural = _("Users")


    def __str__(self):
        return self.first_name + " " + self.last_name


    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    language = models.CharField(max_length=3, choices=settings.LANGUAGES, verbose_name= _('Language'), default= 'en', null= False, blank= False)
    theme = models.CharField(max_length=25, choices=settings.THEMES, verbose_name= _('Theme'), default= 'winter', null= False, blank= False)
    image = models.ImageField( upload_to='', verbose_name= _('Image'), default='user.png') 


    def __str__(self):
        return f'{self.user.first_name } { self.user.last_name} {_("profile")}'
        #return self.user.first_name + " " + self.user.last_name + " profile"
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

