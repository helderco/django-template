import os
base = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

# Load environment
import dotenv
dotenv.read_dotenv(os.path.join(base, '.env'))

# Get WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
