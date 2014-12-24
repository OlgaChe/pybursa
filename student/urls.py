from django.conf.urls import patterns, include, url
from student.views import students_list, students_item , student_edit


urlpatterns = patterns('',
    url(r'^/$', students_list, name = 'students_list'),
    url(r'^/(?P<student_id>\d+)/$', students_item, name = 'students_item'),
)
