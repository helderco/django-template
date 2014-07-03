# Load environment
import dotenv
dotenv.read_dotenv()

# Get WSGI handler
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
