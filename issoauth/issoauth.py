import re
import jwt
import json
import base64
import logging
import requests
from requests.auth import HTTPBasicAuth


logger = logging.getLogger(__name__)


def decode_base64(data: bytes, altchars=b'+/') -> bytes:
    """Decode base64, padding being optional.

    :param altchars:
    :param data: Base64 data as an ASCII byte string
    :returns: The decoded byte string.

    """
    data = re.sub(rb'[^a-zA-Z0-9%s]+' % altchars, b'', data)  # normalize
    missing_padding = len(data) % 4
    if missing_padding:
        data += b'=' * (4 - missing_padding)
    return base64.b64decode(data, altchars)


def get_json_from_base64(data: str) -> dict:
    data = decode_base64(data.encode("utf-8"))
    return json.loads(data.decode("utf-8"))


class ISSOAuth(object):
    """
    Internal Single Sign-on Authentication
    """
    def __init__(self, **kwargs):
        self.base_url = ""
        self.token_path = "/oauth2/token"
        self.jwks_path = "/.well-known/jwks.json"

        self.setup(**kwargs)
        self._jwks_cache = {}

    def setup(self, **kwargs):
        self.base_url = kwargs.get('base_url', '')
        self.token_path = kwargs.get('token_path', '/oauth2/token')
        self.jwks_path = kwargs.get('jwks_path', '/.well-known/jwks.json')

    def has_permission(self, token, scope, **kwargs):
        payload = self.verify_token(token, **kwargs)
        return self.is_scope_exists(scope, payload)

    @classmethod
    def is_scope_exists(cls, scope, token_payload):
        if 'scp' in token_payload:
            scope_data_list = []
            scope_data = token_payload["scp"]

            if type(scope_data) == str:
                scope_data_list = scope_data.split(" ")

            if type(scope_data) == list:
                scope_data_list = scope_data

            if scope in scope_data_list:
                return True

        if 'scope' in token_payload:
            scope_data_list = []
            scope_data = token_payload["scope"]

            if type(scope_data) == str:
                scope_data_list = scope_data.split(" ")

            if type(scope_data) == list:
                scope_data_list = scope_data

            if scope in scope_data_list:
                return True

        return False

    def get_token(self, **kwargs):
        client_id = kwargs.get("client_id")
        client_secret = kwargs.get("client_secret")
        scope = kwargs.get("scope", [])
        audience = kwargs.get("audience", [])

        if type(scope) == list:
            scope = " ".join(scope)
        elif type(scope) == str:
            scope = scope

        data = {
            "scope": scope,
            "audience": " ".join(audience),
            "grant_type": "client_credentials"
        }

        r = requests.post(self.base_url + self.token_path, data, auth=HTTPBasicAuth(client_id, client_secret))
        if r.status_code == 200:
            return r.json()
        else:
            return {}

    def get_jwks(self):
        r = requests.get(self.base_url + self.jwks_path)
        if r.status_code == 200:
            return r.json()
        else:
            return {}

    def _derive_key(self, kid) -> (bool, dict):
        if self._jwks_cache == {}:
            self._jwks_cache = self.get_jwks()
            logger.info(f"JWKS loaded {self.jwks_path}")

        selected_key = {}
        for single_key in self._jwks_cache["keys"]:
            if single_key["kid"] == kid:
                selected_key = single_key
        if selected_key == {}:
            return False, {}

        return True, selected_key

    def verify_token(self, token, **kwargs) -> dict:
        try:
            token_data = token.split(".")
            header = get_json_from_base64(token_data[0])
            kid = header["kid"]

            found, selected_key = self._derive_key(kid)
            if not found:
                found, selected_key = self._derive_key(kid)
                if not found:
                    return {}

            return self.get_token_payload_with_key(token,
                                                   selected_key,
                                                   kwargs.get("audience", ""),
                                                   kwargs.get("issuer", ""))

        except Exception as e:
            logger.exception(e)

        return {}

    @classmethod
    def get_token_payload_with_key(cls, token: str,
                                   selected_key: dict,
                                   audience: str,
                                   issuer: str) -> dict:
        # token_data = token.split(".")
        # header = get_json_from_base64(token_data[0])
        #
        # kid = header["kid"]
        # selected_key = {}
        # for single_key in jwks["keys"]:
        #     if single_key["kid"] == kid:
        #         selected_key = single_key
        #
        # if selected_key == {}:
        #     return {}

        key = None
        if selected_key['kty'] == 'RSA':
            key = jwt.algorithms.RSAAlgorithm.from_jwk(json.dumps(selected_key))

        extras = {}
        if len(audience) != 0:
            extras['audience'] = audience
        if len(issuer) != 0:
            extras['issuer'] = issuer

        options = dict(
            verify_iat=True,
            verify_aud='audience' in extras,
            verify_nbf=True,
            verify_exp=True,
        )
        payload = jwt.decode(token, key=key, algorithms=[selected_key['alg']], options=options, **extras)
        return payload


class Singleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(**kwargs)
            return cls._instances[cls]
        else:
            c = cls._instances[cls]
            c.setup(**kwargs)
            return c


class ISSOAuthSingleton(ISSOAuth, metaclass=Singleton):
    def __init__(self, **kwargs):
        super(ISSOAuthSingleton, self).__init__(**kwargs)
