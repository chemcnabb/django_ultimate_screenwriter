from django.db import models
from django.contrib.auth.models import User
from ultimate_screenwriter.unique_slug import unique_slugify

class Action(models.Model):
    id = models.AutoField(primary_key=True, db_column='ActionID') # Field name made lowercase.
    action = models.TextField(db_column='Action', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'action'

class Character(models.Model):
    id = models.AutoField(primary_key=True, db_column='CharacterID') # Field name made lowercase.
    name = models.CharField(max_length=765, db_column='CharacterName') # Field name made lowercase.
    class Meta:
        db_table = u'character'

class Dialogue(models.Model):
    id = models.AutoField(primary_key=True, db_column='DialogueID') # Field name made lowercase.
    dialogue_text = models.TextField(db_column='DialogueText', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'dialogue'

class Parentheses(models.Model):
    id = models.AutoField(primary_key=True, db_column='ParenthesesID') # Field name made lowercase.
    parentheses = models.TextField(db_column='ParenthesesText', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'parentheses'

class Screenplay(models.Model):
    id = models.AutoField(primary_key=True, db_column='ScreenplayID') # Field name made lowercase.
    user = models.ForeignKey(User, blank=True, null=True)
    name = models.CharField(max_length=765, db_column='Title', blank=True) # Field name made lowercase.
    author = models.CharField(max_length=765, db_column='Author', blank=True) # Field name made lowercase.
    date = models.DateTimeField(auto_now_add=True, db_column='Date', blank=True) # Field name made lowercase.
    screenplay_document = models.FileField(upload_to='uploaded_screenplays/%Y/%m/%d', null=True)
    slug = models.SlugField(blank=True, null=True, help_text="This will be auto generated from the title (and it will be unique).")
    class Meta:
        db_table = u'screenplay'


    def get_absolute_url(self):
        return "/screenplay/%s/" % (self.slug)

    def __unicode__(self):
        return "%s" % (self.name)

    def save(self, *args, **kwargs):
        if self.slug == "":
            # Newly created object, so set slug
            self.slug = unique_slugify(self, self.name)
        super(Screenplay, self).save(*args, **kwargs)

class Slug(models.Model):
    id = models.AutoField(primary_key=True, db_column='SlugID') # Field name made lowercase.
    slugfield = models.TextField(db_column='Slug', blank=True) # Field name made lowercase.
    class Meta:
        db_table = u'slug'

class ScreenplayElements(models.Model):
    id = models.AutoField(primary_key=True, db_column='ScreenplayElementsID') # Field name made lowercase.
    element_id = models.TextField(db_column='ElementID', blank=True) # Field name made lowercase.
    element_type = models.ForeignKey('ScreenplayElementType')
    parent = models.ForeignKey('ScreenplayElements', blank=True, null=True, related_name="children")
    screenplay = models.ForeignKey('Screenplay')
    sort_order = models.IntegerField(db_column='ScreenplaySortOrder')
    class Meta:
        db_table = u'screenplay_elements'

class ScreenplayElementType(models.Model):
    id = models.AutoField(primary_key=True, db_column='ScreenplayElementTypeID') # Field name made lowercase.
    name = models.CharField(db_column='ElementType', max_length=1000) # Field name made lowercase.
    class Meta:
        db_table = u'screenplay_element_type'

class Act(models.Model):
    screenplay = models.ForeignKey(Screenplay)
    number = models.IntegerField("Act Number", blank=True, null=True)

class Sequence(models.Model):
    act = models.ForeignKey(Act)
    number = models.IntegerField("Sequence Number", blank=True, null=True)
    name = models.CharField("Sequence Name", blank=True, null=True, max_length=255)

class Scene(models.Model):
    sequence = models.ForeignKey(Sequence)
    heading = models.ForeignKey(Slug)
    number = models.IntegerField("Scene Number", blank=True, null=True)
    action = models.TextField("Action", blank=True, null=True)

class Genre(models.Model):
    name = models.CharField(max_length=255) # Field name made lowercase.
