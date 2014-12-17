from django.contrib import admin

from dossier.models import Dossier

@admin.register(Dossier)
class DossierAdmin(admin.ModelAdmin):
    radio_fields = {'address': admin.HORIZONTAL, 'fav_color': admin.HORIZONTAL}
    filter_horizontal = ['un_courses']
    save_as = True
    save_on_top = True
