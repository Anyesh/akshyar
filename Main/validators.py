from django.core.exceptions import ValidationError
from django.core.validators import URLValidator

def validate_url(value):
	url_validator = URLValidator()
	value_1_invalid = False
	value_2_invalid = False
	try:
		url_validator(value)
	except:
		value_1_invalid = True
	value_2_url = f"https://{value}"
	try: 
		url_validator(value_2_url)
	except:
		value_2_invalid = True
	if value_1_invalid and value_2_invalid:
		raise ValidationError("Error")
	return value

def validate_com(value):
	if "com" not in value:
		raise ValidationError("Invalid URL(No .com)")
	return value
