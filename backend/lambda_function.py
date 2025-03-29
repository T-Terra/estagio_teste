import os
import django
from django.core.wsgi import get_wsgi_application
import awsgi 
# Define as variáveis de ambiente do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

# Inicializa o Django
django.setup()

# Gera o aplicativo WSGI do Django
application = get_wsgi_application()

# Este será o ponto de entrada da função Lambda
def lambda_handler(event, context):
    return awsgi.response(application, event, context)
