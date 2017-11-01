from django import forms
from .validators import validate_url


class SubmitUrlForm(forms.Form):
	url = forms.CharField(label='',
						widget= forms.TextInput( attrs = {'placeholder': 'Paste a link to shorten it', 'class' : 'form-control'}),
						validators=[validate_url])


    
	# def clean(self):
	# 	cleaned_data = super(SubmitUrlForm, self).clean()


	# def clean_url(self): 
	# 	url = self.cleaned_data['url']
	# 	url_validator = URLValidator()
	# 	try:
	# 		url_validator(url)
	# 	except:
	# 		raise forms.ValidationError("Invalid URL")
	# 	return url