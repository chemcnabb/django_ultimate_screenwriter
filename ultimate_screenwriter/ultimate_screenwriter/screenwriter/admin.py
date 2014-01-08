from django.contrib import admin
from models import Screenplay, Act, Sequence, Slug, Character, Scene, Action, Dialogue, ScreenplayElements, ScreenplayElementType, Parentheses
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

class SlugAdmin(admin.ModelAdmin):
    pass
admin.site.register(Slug, SlugAdmin)

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

class ScreenplayElementsAdmin(admin.ModelAdmin):
    pass
class ParenthesesAdmin(admin.ModelAdmin):
    pass
class ScreenplayElementTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ScreenplayElements, ScreenplayElementsAdmin)
admin.site.register(Parentheses, ParenthesesAdmin)
admin.site.register(ScreenplayElementType, ScreenplayElementTypeAdmin)
