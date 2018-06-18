# -*- coding: utf-8 -*-
import datetime
import uuid

from django.conf import settings
from django.core.cache import caches

from eTicket import krypt

conn = caches['default']


def generate_hash():
    """
    Generates a random hash using the uuid4 module
    """

    return str(uuid.uuid4())


def create_client_access_token(key, secret, name, expires_after_days=30):
    """
    Creates an access_token for an API client
    based on the key, secret and timestamp.

    Encryption Algo used from krypt script.
    """

    # First we try to get the token from the redis cache
    # if the token exists we directly return the token
    tdata = conn.get('%s%s%s' % (key, settings.DEFAULT_SEP, secret))
    if tdata:
        token = tdata.get('token')
        expires_on = tdata.get('expires_on')
        iv = tdata.get('iv')
        tag = tdata.get('tag')

        return iv, token, tag, expires_on

    # If token does not exist in the cache create a new token
    # and then put it in the cache
    name_in_byte = name
    now = datetime.datetime.now()
    expires_on = now + datetime.timedelta(expires_after_days)
    cache_expire = int((expires_on - now).total_seconds())
    expires_on = expires_on.strftime(settings.DATE_FORMAT)

    raw_token_key = '%s%s%s%s%s' % (key, settings.DEFAULT_SEP, secret,
                                    settings.DEFAULT_SEP, expires_on)
    iv, token, tag = krypt.encrypt(b"123456desire9000", raw_token_key.encode(), name_in_byte.encode())

    # Save the newly created token in the cache
    # and expire the entry on expires_on value
    cache_map = {'token': token, 'expires_on': expires_on}
    conn.set('%s%s%s' % (key, settings.DEFAULT_SEP, secret), cache_map,
             timeout=cache_expire)

    return iv, token, tag, expires_on


def client_access_token_valid(iv, access_token, tag, name):
    """
    Returns a boolean value of whether or not
    a given client access token is valid
    """

    try:
        raw_token = krypt.decrypt(b"123456desire9000", name, iv, access_token, tag)
    except (TypeError, ValueError, Exception) as err:
        raw_token = ""

    raw_split = raw_token.split(settings.DEFAULT_SEP)

    if len(raw_split) == 3:
        key, secret, expires_on = raw_split
        tdata = conn.get('%s%s%s' % (key, settings.DEFAULT_SEP, secret))

        if tdata:
            return tdata.get('token') == access_token

    return False
