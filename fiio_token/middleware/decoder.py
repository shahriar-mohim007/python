from fiio_token.token.decoder import decode_authorization_token
from fiio_token.token.decoder import decode_transaction_token
from fiio_token.token.decoder import decode_service_authorization_token


class AuthorizationTokenDecoder(object):
    """ AuthorizationTokenDecoder """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        fiio_token = decode_authorization_token(request)

        if len(fiio_token) != 0:
            request.fiio_token = fiio_token

        response = self.get_response(request)
        return response


class ServiceAuthorizationTokenDecoder(object):
    """ ServiceAuthorizationTokenDecoder """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        fiio_service_token = decode_service_authorization_token(request)

        if len(fiio_service_token) != 0:
            request.fiio_service_token = fiio_service_token

        response = self.get_response(request)
        return response


class TransactionTokenDecoder(object):
    """ TransactionTokenDecoder """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request, *args, **kwargs):
        fiio_transaction_token = decode_transaction_token(request)

        if len(fiio_transaction_token) != 0:
            request.fiio_transaction_token = fiio_transaction_token

        response = self.get_response(request)
        return response
