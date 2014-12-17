from django.contrib import admin

from coaches.models import Coach

@admin.register(Coach)
class CoachAdmin(admin.ModelAdmin):
    list_display = ['name','surname', 'email', 'phone']
    radio_fields = {'job': admin.HORIZONTAL, 'dossier': admin.HORIZONTAL}
    save_as = True
    save_on_top = True

