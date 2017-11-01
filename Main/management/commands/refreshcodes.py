from django.core.management.base import BaseCommand, CommandError
from Main.models import AakshyarURL

class Command(BaseCommand):
    help = 'refreshes all the shortcodes'

    def add_arguments(self, parser):
        parser.add_argument('--items', type=int)

    def handle(self, *args, **options):
        print(options)
        return AakshyarURL.objects.refresh_shortcodes(items=options['items'])
