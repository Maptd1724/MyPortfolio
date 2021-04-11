from django.contrib import admin

# Register your models here.
from .models import Skill

class SkillAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'is_published')
    list_display_links = ('id', 'title')
    list_editable = ('is_published',)
    list_per_page = 25

admin.site.register(Skill, SkillAdmin)
