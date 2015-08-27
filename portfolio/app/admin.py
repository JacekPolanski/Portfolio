from django.contrib import admin

from .models import AboutMe, Project, Community, Contact, Skill

admin.site.register(AboutMe)
admin.site.register(Project)
admin.site.register(Community)
admin.site.register(Contact)
admin.site.register(Skill)
