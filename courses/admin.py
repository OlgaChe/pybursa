from django.contrib import admin

from courses.models import Course

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_filter = ['start_date', 'end_date']
    radio_fields = {'coach': admin.HORIZONTAL, 'assistant': admin.HORIZONTAL, 'technology': admin.HORIZONTAL, 'venue': admin.HORIZONTAL}
    save_as = True
    save_on_top = True

