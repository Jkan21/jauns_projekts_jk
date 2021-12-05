from django.contrib import admin
from .models import Visit
# Register your models here.

class VisitAdmin(admin.ModelAdmin):
    pass


admin.site.register(Visit, VisitAdmin)


