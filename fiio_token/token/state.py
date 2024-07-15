import base64

from django.conf import settings

from .backends import TokenBackend

FIIO_TOKEN = settings.FIIO_TOKEN

JWT_ALGORITHM = FIIO_TOKEN['JWT_ALGORITHM']
JWT_SIGNING_KEY = FIIO_TOKEN['JWT_SIGNING_KEY']
JWT_VERIFYING_KEY = FIIO_TOKEN['JWT_VERIFYING_KEY']
JWT_AUDIENCE = FIIO_TOKEN['JWT_AUDIENCE']
JWT_ISSUER = FIIO_TOKEN['JWT_ISSUER']

if not JWT_ALGORITHM.startswith('HS'):
    if len(JWT_SIGNING_KEY) != 0:
        JWT_SIGNING_KEY = base64.decodebytes(str(JWT_SIGNING_KEY).encode("utf-8"))

if not JWT_ALGORITHM.startswith('HS'):
    if len(JWT_VERIFYING_KEY) != 0:
        JWT_VERIFYING_KEY = base64.decodebytes(str(JWT_VERIFYING_KEY).encode("utf-8"))

token_backend = TokenBackend(
    JWT_ALGORITHM,
    JWT_SIGNING_KEY,
    JWT_VERIFYING_KEY,
    JWT_AUDIENCE,
    JWT_ISSUER
)
