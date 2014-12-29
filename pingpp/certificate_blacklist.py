import hashlib

from pingpp.error import APIError


BLACKLISTED_DIGESTS = [
    '05c0b3643694470a888c6e7feb5c9e24e823dc531',
    '5b7dc7fbc98d78bf76d4d4fa6f597a0c901fad5c'
]


def verify(certificate):
    """Verifies a PEM encoded certificate against a blacklist of known revoked
    fingerprints.

    returns True on success, raises RuntimeError on failure.
    """
    sha = hashlib.sha1()
    sha.update(certificate)
    fingerprint = sha.hexdigest()

    if fingerprint in BLACKLISTED_DIGESTS:
        raise APIError("Invalid server certificate. You tried to "
                       "connect to a server that has a revoked "
                       "SSL certificate, which means we cannot "
                       "securely send data to that server. "
                       "Please email support@pingxx.com if you "
                       "need help connecting to the correct API "
                       "server.")
    return True
