from django.contrib import admin
from .models import PersonalDetail, Education, Skill, Project, ContactMessage

# Personal Details Admin
@admin.register(PersonalDetail)
class PersonalDetailAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "phone", "location")
    search_fields = ("name", "email")

# Education Admin
@admin.register(Education)
class EducationAdmin(admin.ModelAdmin):
    list_display = ("degree", "institution", "year")
    search_fields = ("degree", "institution")

# Skills Admin
@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "proficiency")
    list_filter = ("proficiency",)

# Projects Admin
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "github_link", "live_demo")
    search_fields = ("title",)
    list_filter = ("title",)

# Contact Messages Admin
@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "created_at")
    search_fields = ("name", "email", "subject")
    list_filter = ("created_at",)
    readonly_fields = ("created_at",)
