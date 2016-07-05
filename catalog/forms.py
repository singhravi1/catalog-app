from django import forms
from django.forms import ModelForm
from .models import Books,Music

class bookform(forms.ModelForm):
	class Meta:
		model=Books
		exclude=()


class musicform(forms.ModelForm):
	class Meta:
		model=Music
		exclude=()