import os
import django
import logging
from django.core.wsgi import get_wsgi_application
import awsgi

# Configuração do logging para depuração
logging.basicConfig(level=logging.INFO)

try:
    # Definir as variáveis de ambiente do Django
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

    # Inicializa o Django
    django.setup()

    # Gera o aplicativo WSGI do Django
    application = get_wsgi_application()

    # Log de sucesso da inicialização
    logging.info("Django inicializado com sucesso.")

except Exception as e:
    logging.error("Erro ao inicializar o Django: %s", str(e))
    raise e

# Este será o ponto de entrada da função Lambda
def lambda_handler(event, context):
    try:
        # Retorna a resposta usando o awsgi
        response = awsgi.response(application, event, context)
        logging.info("Resposta gerada com sucesso.")
        return response
    except Exception as e:
        logging.error("Erro durante a execução do Lambda: %s", str(e))
        raise e

