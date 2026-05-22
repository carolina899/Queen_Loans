"""
WSGI config for Queen_Loans project.
"""

import os
import logging
from django.core.wsgi import get_wsgi_application

# =========================================================
# VARIABLES DE ENTORNO
# =========================================================
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Queen_Loans.settings')

# =========================================================
# LOGGING BÁSICO
# =========================================================
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

logger = logging.getLogger(__name__)
logger.info("Iniciando aplicación Queen Loans...")

# =========================================================
# WSGI APPLICATION
# =========================================================
application = get_wsgi_application()

logger.info("WSGI cargado correctamente.")
