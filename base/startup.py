from django.core.exceptions import MiddlewareNotUsed
from django.conf import settings
from django.core.management import call_command

class StartupMiddleware(object):
    def __init__(self):
        # The following db settings name is django 1.2.  django < 1.2 will use settings.DATABASE_NAME
        if settings.DATABASES['default']['NAME'] == ':memory:':
            call_command('syncdb', interactive=False)

        raise MiddlewareNotUsed('Startup complete')
