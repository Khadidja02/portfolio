from django.contrib import admin

# Register your models here.
from .models import AboutMe, Skills, Services, Portfolio, ContactForm, ProjectImage

class AboutMeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'profession', 'email', 'phone_number')
    search_fields = ('first_name', 'last_name', 'profession', 'email')

class SkillsAdmin(admin.ModelAdmin):
    list_display = ('skill_name',)
    search_fields = ('skill_name',)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ('service_name',)
    search_fields = ('service_name',)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ('project_title', 'category', 'project_url')
    search_fields = ('project_title', 'category')

class ContactFormAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject')
    search_fields = ('name', 'email', 'subject')

# Register your models here.
admin.site.register(AboutMe, AboutMeAdmin)
admin.site.register(Skills, SkillsAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(Portfolio, PortfolioAdmin)
admin.site.register(ContactForm, ContactFormAdmin)
admin.site.register(ProjectImage)