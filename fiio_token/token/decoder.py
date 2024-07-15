import logging

from django.conf import settings
from rest_framework import HTTP_HEADER_ENCODING
from rest_framework.request import Request

from fiio_token.token.exceptions import TokenError
from fiio_token.token.tokens import AnyToken, TransactionToken

logger = logging.getLogger(__name__)

try:
    from issoauth.issoauth import ISSOAuthSingleton
    ISSO_AUTH_BASE_URL = settings.ISSO_URL
except Exception as gex:
    logger.error(gex)


FIIO_TOKEN = settings.FIIO_TOKEN

AUTH_HEADER_TYPES = FIIO_TOKEN['JWT_AUTH_HEADER_TYPES']

if not isinstance(AUTH_HEADER_TYPES, (list, tuple)):
    AUTH_HEADER_TYPES = (AUTH_HEADER_TYPES,)

AUTH_HEADER_TYPE_BYTES = set(
    str(h).lower().encode(HTTP_HEADER_ENCODING)
    for h in AUTH_HEADER_TYPES
)


def parse_authorization_header(request: Request) -> dict:
    try:
        return __parse_authorization_header__(request)
    except Exception as e:
        logger.error(e)
    return {}


def __parse_authorization_header__(request: Request) -> dict:
    auth_header = get_header(request)
    raw_token = get_raw_token(auth_header)
    if len(raw_token) == 0:
        return {}

    try:
        token = AnyToken(token=raw_token)
        return token.payload
    except TokenError as e:
        logger.error(e)
        return {}


def get_header(request: Request):
    """
    Extracts the header containing the JSON web token from the given
    request.
    """
    header = request.META.get('HTTP_AUTHORIZATION')

    if isinstance(header, str):
        # Work around django test client oddness
        header = header.encode(HTTP_HEADER_ENCODING)

    return header


def get_raw_token_tuple(header) -> (str, str):
    """
    Extracts an unvalidated JSON web token from the given "Authorization"
    header value.
    """
    if header is None:
        return '', ''

    if len(header) == 0:
        return '', ''

    parts = header.split()

    if len(parts) == 0:
        # Empty AUTHORIZATION header sent
        return '', ''

    if parts[0].decode(HTTP_HEADER_ENCODING).lower().encode(HTTP_HEADER_ENCODING) not in AUTH_HEADER_TYPE_BYTES:
        # Assume the header does not contain a JSON web token
        return '', ''

    if len(parts) != 2:
        return '', ''

    return parts[0].decode('utf-8'), parts[1].decode('utf-8')


def get_raw_token(header) -> str:
    """
    Extracts an unvalidated JSON web token from the given "Authorization"
    header value.
    """
    return get_raw_token_tuple(header)[1]


def get_auth_payload(request: Request) -> dict:
    return parse_authorization_header(request)


def decode_auth_payload(request: Request) -> dict:
    return parse_authorization_header(request)


def get_authorization_header(request: Request) -> dict:
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if len(auth_header) == 0:
        return {}
    return decode_any_token(auth_header)


def decode_authorization_token(request: Request) -> dict:
    auth_header = request.META.get('HTTP_AUTHORIZATION', '')
    if len(auth_header) == 0:
        return {}
    return decode_any_token(auth_header)


def decode_service_authorization_token(request: Request) -> dict:
    auth_header = request.META.get('HTTP_X_SERVICE_AUTHORIZATION', '')
    if len(auth_header) == 0:
        return {}
    return decode_any_token(auth_header)


def decode_transaction_token(request: Request) -> dict:
    transaction_token_header = request.META.get('HTTP_X_TRANSACTION_TOKEN', '')

    if len(transaction_token_header) == 0:
        return {}

    if isinstance(transaction_token_header, str):
        # Work around django test client oddness
        transaction_token_header = transaction_token_header.encode(HTTP_HEADER_ENCODING)

    raw_token = get_raw_token(transaction_token_header)

    if len(raw_token) == 0:
        return {}

    try:
        token = TransactionToken(token=raw_token, verify=True)
        return token.payload
    except TokenError as ex:
        logger.error(ex)
        return {}


def decode_any_token(auth_header) -> dict:
    if isinstance(auth_header, str):
        # Work around django test client oddness
        auth_header = auth_header.encode(HTTP_HEADER_ENCODING)
    token_bearer, raw_token = get_raw_token_tuple(auth_header)
    if len(raw_token) == 0:
        return {}

    if token_bearer.lower() == "jwt":
        logger.info("using internal jwt decoder")
        try:
            token = AnyToken(token=raw_token)
            return token.payload
        except TokenError as e:
            logger.error(e)
            return {}
    else:
        logger.info("using external sso jwt decoder")
        try:
            sso = ISSOAuthSingleton(base_url=ISSO_AUTH_BASE_URL)
            return sso.verify_token(raw_token)
        except Exception as e:
            logger.error(e)
            return {}
