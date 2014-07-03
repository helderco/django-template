from django.core.wsgi import get_wsgi_application
from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
from dj_static import Cling

application = Sentry(Cling(get_wsgi_application()))
