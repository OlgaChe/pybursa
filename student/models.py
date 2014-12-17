from django.db import models

from django import forms

from courses.models import Course
from dossier.models import Dossier


class Student(models.Model):

    PACKAGE_CHOICES = (('s', 'Standard'), ('g', 'Gold'), ('p', 'Platinum'))
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    date_of_birth = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    courses = models.ManyToManyField(Course, blank=True)
    package = models.CharField(max_length=1, choices=PACKAGE_CHOICES, default='s')
    dossier = models.OneToOneField(Dossier, null=True)

    def __unicode__(self):
        return "%s %s" % (self.first_name, self.last_name)

class StudentForm(forms.Form):
    CHOICES= (('vip', 'vip'),('standart', 'standart'),('gold', 'gold'),)
    student_name = forms.CharField(max_length=100)
    student_package = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
