from django.contrib import admin
from models import Screenplay, Act, Sequence, Heading, Character, Scene, Action, Dialogue
# Register your models here.



class ScreenplayAdmin(admin.ModelAdmin):
    pass
admin.site.register(Screenplay, ScreenplayAdmin)

class ActAdmin(admin.ModelAdmin):
    pass
admin.site.register(Act, ActAdmin)

class SequenceAdmin(admin.ModelAdmin):
    pass
admin.site.register(Sequence, SequenceAdmin)

class HeadingAdmin(admin.ModelAdmin):
    pass
admin.site.register(Heading, HeadingAdmin)

class CharacterAdmin(admin.ModelAdmin):
    pass
admin.site.register(Character, CharacterAdmin)

class SceneAdmin(admin.ModelAdmin):
    pass
admin.site.register(Scene, SceneAdmin)

class ActionAdmin(admin.ModelAdmin):
    pass
admin.site.register(Action, ActionAdmin)

class DialogueAdmin(admin.ModelAdmin):
    pass
admin.site.register(Dialogue, DialogueAdmin)
