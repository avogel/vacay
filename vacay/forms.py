from django import forms
from vacay.vposts.models import VisitedDay
from django.contrib.auth.forms import UserCreationForm

class BlogForm(forms.Form):
	title = forms.CharField(max_length=200)
	contents = forms.CharField(widget=forms.Textarea)
	day = forms.ModelChoiceField(queryset = VisitedDay.objects.all())

class TestForm(forms.Form):
	num = forms.CharField()

class NewTripForm(forms.Form):
	name = forms.CharField(max_length=100)
	description = forms.CharField(widget=forms.Textarea)
	start_date = forms.DateField(input_formats=['%m-%d-%Y'], required=False)

	def __init__(self, *args, **kwargs):
		if 'city_list' in kwargs:
			city_list = kwargs.pop('city_list')
		else:
			city_list = []
		super(NewTripForm, self).__init__(*args, **kwargs)

		i = 1
		for (city_name, num_days, overlap) in city_list:
			self.fields['city_name%s' % i] = forms.CharField()
			self.fields['num_days%s' % i] = forms.IntegerField()
			self.fields['overlap%s' % i] = forms.BooleanField(required=False)
			i += 1
		self.num_cities = i - 1
		# if self.num_cities < 0:
		# 	raise forms.ValidationError("You must visit at least one city!")

class ContactForm(forms.Form):
    subject = forms.CharField(max_length=100)
    email = forms.EmailField(required=False)
    message = forms.CharField(widget=forms.Textarea)

class RegistrationForm(UserCreationForm):
	email = forms.EmailField()
	first_name = forms.CharField(max_length=30)
	last_name = forms.CharField(max_length=30)
