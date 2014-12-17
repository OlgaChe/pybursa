from django.contrib import admin
from student.models import Student

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ['name', 'surname']
    exclude = ['surname']
    filter_vertical = ['courses']
    filter_horizontal = ['courses']
    radio_fields = {'package': admin.HORIZONTAL}
    readonly_fields = ['package']
    save_as = True
    save_on_top = True

#admin.site.register(Student, StudentAdmin)
