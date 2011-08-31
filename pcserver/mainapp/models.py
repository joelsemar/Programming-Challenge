import sys
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import ModelBase
from django.db.models.signals import post_save
from django.dispatch import receiver
import base64
# Create your models here.
class Term(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __unicode__(self):
        return self.title
    
    def image_url(self):
        return self.image and self.image.url or ''


class Token(models.Model):
    user = models.ForeignKey(User)
    string = models.CharField(max_length=256,default='')

    def save(self, *args, **kwargs):
        self.string = base64.b64encode("%s:%s" % (self.user.username, self.user.password))
        super(Token, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return "Token: %s" % self.user.username


@receiver(post_save, sender=User)
def create_token(sender, **kwargs):
    if kwargs.get('created'):
        user = kwargs.get('instance')
        Token.objects.create(user=user)

#ALL DEFINITION EOF
module_name = globals().get('__name__')
models = sys.modules[module_name]
models._all_ = []
for model_name in dir():
    m = getattr(models, model_name)
    if isinstance(m, ModelBase) and not m._meta.abstract:
        models._all_.append(model_name)
