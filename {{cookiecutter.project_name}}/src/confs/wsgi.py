# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Load environment variables
from unipath import Path
BASE_DIR = Path(__file__).absolute().ancestor(3)
try:
    import dotenv
    env_file = BASE_DIR.child('.env')
    if env_file.exists():
        dotenv.read_dotenv(env_file)
except ImportError:
    pass

# Get WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

# Sentry?
try:
    from raven.contrib.django.raven_compat.middleware.wsgi import Sentry
    application = Sentry(application)
except ImportError:
    pass
