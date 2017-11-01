from django.db import models
from Main.models import AakshyarURL


class ClickEventManager(models.Manager):
	def create_event(self, A_instance):
		if isinstance(A_instance, AakshyarURL):
			obj, created = self.get_or_create(url = A_instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None



class ClickEvent(models.Model):
	url = models.OneToOneField(AakshyarURL)
	count = models.IntegerField(default = 0)
	updated = models.DateTimeField(auto_now = True)
	timestamp = models.DateTimeField(auto_now_add = True)

	objects = ClickEventManager()

	def __str__(self):
		return "{}".format(self.count)