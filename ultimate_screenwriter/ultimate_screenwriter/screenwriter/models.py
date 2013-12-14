from django.db import models
from django.contrib.auth.models import User
from ultimate_screenwriter.unique_slug import unique_slugify

# Create your models here.
class Screenplay(models.Model): #a collection, arranged for display
    name = models.CharField("Screenplay Title", blank=True, null=True, max_length=255)
    slug = models.SlugField(blank=True, null=True, help_text="This will be auto generated from the title (and it will be unique).")
    length = models.IntegerField("Screenplay Length", default=120, blank=True, null=True)
    user = models.ForeignKey(User, blank=True, null=True)
    poster = models.ImageField("Movie Poster", upload_to="posters/", blank=True, null=True)
    description = models.TextField("Description", blank=True, null=True)

    def get_absolute_url(self):
        return "/screenplay/%s/" % (self.slug)

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        if self.slug == "":
            # Newly created object, so set slug
            unique_slugify(self, self.name)
        super(Screenplay, self).save(*args, **kwargs)

class Act(models.Model):
    screenplay = models.ForeignKey(Screenplay)
    number = models.IntegerField("Act Number", blank=True, null=True)

class Sequence(models.Model):
    act = models.ForeignKey(Act)
    number = models.IntegerField("Sequence Number", blank=True, null=True)
    name = models.CharField("Sequence Name", blank=True, null=True, max_length=255)

class Heading(models.Model):
    name = models.CharField("Scene Heading", blank=True, null=True, max_length=255)

class Scene(models.Model):
    sequence = models.ForeignKey(Sequence)
    heading = models.ForeignKey(Heading)
    number = models.IntegerField("Scene Number", blank=True, null=True)
    action = models.TextField("Action", blank=True, null=True)



class Action(models.Model):
    heading = models.ForeignKey(Heading)

class Character(models.Model):
    scene = models.ForeignKey(Scene)
    heading = models.ForeignKey(Heading)
    order = models.IntegerField("Placement Order", blank=True, null=True, default=1)
    name = models.CharField("Character Name", blank=True, null=True, max_length=255)

class Dialogue(models.Model):
    character = models.ForeignKey(Character)



