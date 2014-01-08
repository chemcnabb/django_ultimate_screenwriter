from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.template.defaultfilters import slugify
from datetime import datetime
from models import Screenplay

@receiver(pre_save)
def screenplay_callback(sender, instance, *args, **kwargs):
    try:
        instance.name = instance.screenplay_document.name.split('.')[0]
        instance.slug = slugify(instance.name)
        #read the script

    except AttributeError:
        print "Attribute Error"

