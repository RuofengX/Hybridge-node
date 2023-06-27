from decouple import config
from dotenv import load_dotenv

load_dotenv()


SERVICE_PORT = int(config("SERVICE_PORT", cast=int, default=62050))

XRAY_API_PORT = int(config("XRAY_API_PORT", cast=int, default=62051))
XRAY_EXECUTABLE_PATH = str(
    config("XRAY_EXECUTABLE_PATH", default="/usr/local/bin/xray")
)
XRAY_ASSETS_PATH = str(config("XRAY_ASSETS_PATH", default="/usr/local/share/xray"))

SSL_CERT_FILE = str(
    config("SSL_CERT_FILE", default="/var/lib/marzban-node/ssl_cert.pem")
)
SSL_KEY_FILE = str(config("SSL_KEY_FILE", default="/var/lib/marzban-node/ssl_key.pem"))

DEBUG = bool(config("DEBUG", cast=bool, default=False))
