from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from PIL import Image
from concurrency.fields import TriggerVersionField
from django.core.exceptions import ValidationError



# Create your models here.
class User(AbstractUser):
    user_version = TriggerVersionField(trigger_name='usertrigger')
    

    class Meta:
        
        verbose_name = _("User")
        verbose_name_plural = _("Users")


    def __str__(self):
        return self.first_name + " " + self.last_name
    
    def clean(self):
        if not self._state.adding:
            dbobject = self.__class__.objects.get(pk=self.pk)
            if self.user_version != dbobject.user_version:
                raise ValidationError(_(f'{str(self)} cannot be saved because it has been modified by someone else'))
        super().clean()


    
class Profile(models.Model):
    profile_version = TriggerVersionField(trigger_name='profiletrigger')
    user = models.OneToOneField(User, on_delete= models.CASCADE)
    language = models.CharField(max_length=3, choices=settings.LANGUAGES, verbose_name= _('Language'), default= 'en', null= False, blank= False)
    theme = models.CharField(max_length=25, choices=settings.THEMES, verbose_name= _('Theme'), default= 'winter', null= False, blank= False)
    image = models.ImageField( upload_to='', verbose_name= _('Image'), default='user.png') 


    def __str__(self):
        return f'{self.user.first_name } { self.user.last_name} {_("profile")}'
        #return self.user.first_name + " " + self.user.last_name + " profile"

    def clean(self):
        if not self._state.adding:
            dbobject = self.__class__.objects.get(pk=self.pk)
            if self.profile_version != dbobject.profile_version:
                print(self.profile_version)
                print(dbobject.profile_version)
                raise ValidationError(_(f'{str(self)} cannot be saved because it has been modified by someone else'))
        super().clean()    
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300 :
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)

