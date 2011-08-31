import sys
from django.db import models

from django.db.models.base import ModelBase
# Create your models here.
class Term(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()
    image = models.ImageField(upload_to='images')


    def __unicode__(self):
        return self.title
    
    def image_url(self):
        return self.image and self.image.url or ''

#ALL DEFINITION EOF
module_name = globals().get('__name__')
models = sys.modules[module_name]
models._all_ = []
for model_name in dir():
    m = getattr(models, model_name)
    if isinstance(m, ModelBase) and not m._meta.abstract:
        models._all_.append(model_name)