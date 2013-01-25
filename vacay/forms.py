from django import forms
from vacay.vposts.models import VisitedDay

class BlogForm(forms.Form):
	title = forms.CharField(max_length=200)
	contents = forms.CharField(widget=forms.Textarea)
	day = forms.ModelChoiceField(queryset = VisitedDay.objects.all())

class TestForm(forms.Form):
	num = forms.CharField()
