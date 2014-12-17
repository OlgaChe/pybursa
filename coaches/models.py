from django.contrib.auth.models import User

from django.db import models

from django import forms

from dossier.models import Dossier


class Coach(models.Model):
    COACH_TYPES = (('C', 'Coach'), ('A', 'Assistant'))
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    job = models.CharField(choices=COACH_TYPES, max_length=1)
    #user = models.ForeignKey(User)
    dossier = models.OneToOneField(Dossier, null=True)

    def __unicode__(self):
        return "%s %s (%s)" % (self.name, self.surname, self.job)

class CoachForm(forms.Form):
    CHOICES = (('C', 'Coach'), ('A', 'Assistant'))
    name = forms.CharField(max_length=100)
    package = forms.ChoiceField(widget=forms.RadioSelect, choices=CHOICES)
