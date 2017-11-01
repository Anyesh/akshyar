from django.shortcuts import render, HttpResponseRedirect, get_object_or_404, HttpResponse
from .models import AakshyarURL
from django.views import View
from .forms import SubmitUrlForm
from analytics.models import ClickEvent


class index(View):
	def get(self, request):
		the_form = SubmitUrlForm()
		context = {
			"title" : "Shorten Your URL",
			"form" : the_form
		}
		return render(request, 'Main/index.html', context)

	def post(self, request):
		form = SubmitUrlForm(request.POST)
		context = {
			"title" : "Shorten Your URL",
			"form" : form
		}
		template = 'Main/index.html'
		if form.is_valid():
			submitted_url = form.cleaned_data.get('url')
			obj, created = AakshyarURL.objects.get_or_create(url = submitted_url)
			context = {
				"object" : obj,
				"created" : created
			}
			if created:
				template = 'Main/Success.html'
			else:
				template = 'Main/Exists.html'
		
		return render(request, template, context)

def URLRedirectView(request, shortcode=None, *args, **kwargs):
	obj = get_object_or_404(AakshyarURL, shortcode=shortcode)
	print('this is url', obj)
	print(ClickEvent.objects.create_event(obj))

	return HttpResponseRedirect(obj.url)


	
