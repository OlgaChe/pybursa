from django.db import models

from django import forms

from coaches.models import Coach
from address.models import Address


class Course(models.Model):
    TECHNOLOGY_CHOICE = (('p', 'Python'), ('r', 'Ruby'), ('j', "JavaScript"))
    name = models.CharField(max_length=255)
    description = models.TextField()
    coach = models.ForeignKey(Coach, blank=True, null=True)
    assistant = models.ForeignKey(Coach, blank=True, null=True, related_name="course_assistant")
    start_date = models.DateField()
    end_date = models.DateField()
    technology = models.CharField(max_length=255, choices=TECHNOLOGY_CHOICE)
    venue = models.ForeignKey(Address, blank=True, null=True, related_name="cu_address")

    def __unicode__(self):
        return "%s (%s) - %s" % (self.name, self.coach, self.technology)

class CourseForm(forms.Form):
    class Meta:
         model = Course
         fields = ['name', 'technology', 'coach', 'assistant']
         widgets = {'technology': forms.RadioSelect, 'coach': forms.RadioSelect, 'assistant': forms.RadioSelect}
         labels = {'name': 'Coach name'}
    CHOICES = (('p', 'Python'), ('r', 'Ruby'), ('j', "JavaScript"))
    name = forms.CharField(max_length=100)
    technology = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
    coach = forms.ChoiceField(widget=forms.RadioSelect)
    assistant = forms.ChoiceField(widget=forms.RadioSelect)


