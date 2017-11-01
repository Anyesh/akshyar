from django.db import models
from django.conf import settings
from django_hosts.resolvers import reverse
from .utils import code_generator, create_shortcode
from .validators import validate_url


SHORTCODE_MAX = getattr(settings, "SHORTCODE_MAX", 25)
# SHORTCODE_MAX = settings.SHORTCODE_MAX

class AakshyarURLManager(models.Manager):
	def all(self, *args, **kwargs):
		qs = super(AakshyarURLManager, self).all(*args, **kwargs)
		qs = qs.filter(active = True)

		return qs

	def refresh_shortcodes(self, items=100):
		print(items)
		qs = AakshyarURL.objects.filter(id__gte=1)
		if items is not None and isinstance(items, int):
			qs = qs.order_by('-id')[:items]
		new_codes = 0
		for q in qs:
			q.shortcode = create_shortcode(q)
			print(q.shortcode)
			q.save()
			new_codes += 1
		return "new codes made {}".format(new_codes)

class AakshyarURL(models.Model):
	url = models.CharField(max_length = 220 , validators=[validate_url])
	shortcode = models.CharField(max_length = SHORTCODE_MAX, unique = True, blank=True)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)
	active = models.BooleanField(default=True)

	objects = AakshyarURLManager()

	def __str__(self):
		return str(self.url)

	def save(self, *args, **kwargs):
		if self.shortcode is None or self.shortcode == "":
			self.shortcode = create_shortcode(self)
		if not "http" in self.url:
			self.url = 'http://' + self.url
		super(AakshyarURL, self).save(*args, **kwargs)

	def get_short_url(self):
		url_path = reverse("scode", kwargs={'shortcode' : self.shortcode}, scheme="http")
		return url_path


# class meta:
# 	ordering = '-id'