import ulid
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from fiio_constant.constant.token import TokenType
from .exceptions import TokenBackendError, TokenError
from .utils import (
    aware_utcnow, datetime_from_epoch, datetime_to_epoch, format_lazy,
)

from fiio_constant.constant.wallet import WalletGroup
from fiio_constant.constant.wallet import WalletStatus
from fiio_constant.constant.wallet import WalletPersona
from fiio_constant.constant.wallet import WalletCategory
from fiio_constant.constant.account import AccountType
from fiio_constant.constant.product import ProductType
from fiio_constant.constant.currency import Currency

FIIO_TOKEN = settings.FIIO_TOKEN


def wallet_dictionary(wallet) -> dict:
    groups = [WalletGroup.choice_to_str(g) for g in wallet.groups]
    return {
        'id': wallet.id,
        'cif_id': wallet.cif.id,
        'number': wallet.number,
        'status': WalletStatus.choice_to_str(wallet.status),
        'persona': WalletPersona.choice_to_str(wallet.persona),
        'groups': ",".join(groups),
        'category': WalletCategory.choice_to_str(wallet.category),
        'account_type': AccountType.choice_to_str(wallet.account_type),
        'product_type': ProductType.choice_to_str(wallet.product_type),
        'primary_currency': Currency.choice_to_str(wallet.primary_currency),
        'secondary_currency': Currency.choice_to_str(wallet.secondary_currency)
    }


def wallet_dictionary_simple(wallet) -> dict:
    return {
        'id': wallet.id,
        'cif_id': wallet.cif.id,
        'number': wallet.number,
        'status': wallet.status,
        'persona': wallet.persona,
        'groups': wallet.groups,
        'category': wallet.category,
        'account_type': wallet.account_type,
        'product_type': wallet.product_type,
        'primary_currency': wallet.primary_currency,
        'secondary_currency': wallet.secondary_currency
    }


class TokenBase(object):
    token_type = None
    lifetime = None

    def __init__(self):
        super().__init__()
        self.token = None
        self.current_time = aware_utcnow()
        self.payload = {}

    def __repr__(self):
        return repr(self.payload)

    def __getitem__(self, key):
        return self.payload[key]

    def __setitem__(self, key, value):
        self.payload[key] = value

    def __delitem__(self, key):
        del self.payload[key]

    def __contains__(self, key):
        return key in self.payload

    def get(self, key, default=None):
        return self.payload.get(key, default)

    def __str__(self):
        """
        Signs and returns a token as a base64 encoded string.
        """
        from .state import token_backend

        return token_backend.encode(self.payload)

    def verify(self):
        """
        Performs additional validation steps which were not performed when this
        token was decoded.  This method is part of the "public" API to indicate
        the intention that it may be overridden in subclasses.
        """
        # According to RFC 7519, the "exp" claim is OPTIONAL
        # (https://tools.ietf.org/html/rfc7519#section-4.1.4).  As a more
        # correct behavior for authorization tokens, we require an "exp"
        # claim.  We don't want any zombie tokens walking around.
        self.check_exp()

        # Ensure token id is present
        if 'jti' not in self.payload:
            raise TokenError(_('Token has no id'))

        self.verify_token_type()

    def verify_token_type(self):
        """
        Ensures that the token type claim is present and has the correct value.
        """
        try:
            token_type = self.payload['token_type']
        except KeyError:
            raise TokenError(_('Token has no type'))

        if self.token_type != token_type:
            raise TokenError(_('Token has wrong type'))

    def set_jti(self):
        """
        Populates the configured jti claim of a token with a string where there
        is a negligible probability that the same string will be chosen at a
        later time.

        See here:
        https://tools.ietf.org/html/rfc7519#section-4.1.7
        """
        self.payload['jti'] = ulid.new().str

    def get_batch_id(self) -> str:
        return self.payload['jti']

    def set_exp(self, claim='exp', from_time=None, lifetime=None):
        """
        Updates the expiration time of a token.
        """
        if from_time is None:
            from_time = self.current_time

        if lifetime is None:
            lifetime = self.lifetime

        self.payload[claim] = datetime_to_epoch(from_time + lifetime)

    def check_exp(self, claim='exp', current_time=None):
        """
        Checks whether a timestamp value in the given claim has passed (since
        the given datetime value in `current_time`).  Raises a TokenError with
        a user-facing error message if so.
        """
        if current_time is None:
            current_time = self.current_time

        try:
            claim_value = self.payload[claim]
        except KeyError:
            raise TokenError(format_lazy(_("Token has no '{}' claim"), claim))

        claim_time = datetime_from_epoch(claim_value)
        if claim_time <= current_time:
            raise TokenError(format_lazy(_("Token '{}' claim has expired"), claim))

    @classmethod
    def for_wallet(cls, wallet):
        """
        Returns an authorization token for the given user that will be provided
        after authenticating the user's credentials.
        """
        token = cls()
        token['wallet'] = wallet_dictionary_simple(wallet)

        return token


class Token(TokenBase):
    """
    A class which validates and wraps an existing JWT or can be used to build a
    new JWT.
    """
    token_type = None
    lifetime = None

    def __init__(self, token=None, verify=True):
        super().__init__()
        """
        !!!! IMPORTANT !!!! MUST raise a TokenError with a user-facing error
        message if the given token is invalid, expired, or otherwise not safe
        to use.
        """
        if self.token_type is None or self.lifetime is None:
            raise TokenError(_('Cannot create token with no type or lifetime'))

        self.token = token
        self.current_time = aware_utcnow()

        # Set up token
        if token is not None:
            # An encoded token was provided
            from .state import token_backend

            # Decode token
            try:
                self.payload = token_backend.decode(token, verify=verify)
            except TokenBackendError:
                raise TokenError(_('Token is invalid or expired'))

            if verify:
                self.verify()
        else:
            # New token.  Skip all the verification steps.
            self.payload = {'token_type': self.token_type}

            # Set "exp" claim with default value
            self.set_exp(from_time=self.current_time, lifetime=self.lifetime)

            # Set "jti" claim
            self.set_jti()


class WalletUserAccessToken(Token):
    token_type = TokenType.WALLET_USER_ACCESS
    lifetime = FIIO_TOKEN['JWT_WALLET_USER_ACCESS_TOKEN_LIFETIME']


class WalletUserRefreshToken(Token):
    token_type = TokenType.WALLET_USER_REFRESH
    lifetime = FIIO_TOKEN['JWT_WALLET_USER_REFRESH_TOKEN_LIFETIME']
    no_copy_claims = (
        'token_type',
        'exp',
        'jti',
    )

    @property
    def access_token(self) -> WalletUserAccessToken:
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        access = WalletUserAccessToken()

        # Use instantiation time of refresh token as relative timestamp for
        # access token "exp" claim.  This ensures that both a refresh and
        # access token expire relative to the same time if they are created as
        # a pair.
        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access


class ServiceUserAccessToken(Token):
    token_type = TokenType.SERVICE_USER_ACCESS
    lifetime = FIIO_TOKEN['JWT_SERVICE_USER_ACCESS_TOKEN_LIFETIME']


class ServiceUserRefreshToken(Token):
    token_type = TokenType.SERVICE_USER_REFRESH
    lifetime = FIIO_TOKEN['JWT_SERVICE_USER_REFRESH_TOKEN_LIFETIME']


class DeviceAuthorizationToken(Token):
    token_type = TokenType.DEVICE_AUTHORIZATION
    lifetime = FIIO_TOKEN['JWT_DEVICE_AUTHORIZATION_TOKEN_LIFETIME']


class TransactionToken(Token):
    token_type = TokenType.TRANSACTION
    lifetime = FIIO_TOKEN['JWT_TRANSACTION_TOKEN_LIFETIME']
    no_copy_claims_for_wallet = (
        'token_type',
        'exp',
        'jti',
        'scopes',
        'transaction_payload'
    )

    no_copy_claims_for_service = (
        'token_type',
        'exp',
        'jti',
        'scopes',
        'transaction_payload'
    )

    @classmethod
    def for_wallet(cls, wallet):
        token = cls()
        token['wallet'] = wallet_dictionary_simple(wallet)

        return token

    @property
    def access_token_for_wallet(self) -> WalletUserAccessToken:
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        access = WalletUserAccessToken()

        # Use instantiation time of refresh token as relative timestamp for
        # access token "exp" claim.  This ensures that both a refresh and
        # access token expire relative to the same time if they are created as
        # a pair.
        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims_for_wallet
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access

    @property
    def refresh_token_for_wallet(self) -> WalletUserRefreshToken:
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        refresh = WalletUserRefreshToken()

        # Use instantiation time of refresh token as relative timestamp for
        # access token "exp" claim.  This ensures that both a refresh and
        # access token expire relative to the same time if they are created as
        # a pair.
        refresh.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims_for_wallet
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            refresh[claim] = value

        return refresh

    @property
    def access_token_for_service(self) -> ServiceUserAccessToken:
        """
        Returns an access token created from this refresh token.  Copies all
        claims present in this refresh token to the new access token except
        those claims listed in the `no_copy_claims` attribute.
        """
        access = ServiceUserAccessToken()

        # Use instantiation time of refresh token as relative timestamp for
        # access token "exp" claim.  This ensures that both a refresh and
        # access token expire relative to the same time if they are created as
        # a pair.
        access.set_exp(from_time=self.current_time)

        no_copy = self.no_copy_claims_for_service
        for claim, value in self.payload.items():
            if claim in no_copy:
                continue
            access[claim] = value

        return access


class AnyToken(TokenBase):
    token_type = None
    lifetime = None

    def __init__(self, token):
        super().__init__()
        if token is None:
            raise TokenError(_('No token provided'))

        self.token = token
        self.current_time = aware_utcnow()

        # An encoded token was provided
        from .state import token_backend

        # Decode token
        try:
            self.payload = token_backend.decode(token, verify=True)
        except TokenBackendError:
            raise TokenError(_('Token is invalid or expired'))

        self.check_exp()
        if 'jti' not in self.payload:
            raise TokenError(_('Token has no id'))

    def __str__(self) -> str:
        return ''
