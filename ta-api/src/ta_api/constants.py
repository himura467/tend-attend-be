import os

from dotenv import load_dotenv

load_dotenv()

COOKIE_DOMAIN = os.getenv("COOKIE_DOMAIN")

ACCESS_TOKEN_NAME = "acctkn"
REFRESH_TOKEN_NAME = "reftkn"
