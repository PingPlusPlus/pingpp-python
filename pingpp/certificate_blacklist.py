import hashlib

from pingpp.error import APIError


BLACKLISTED_DIGESTS = [
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
                       "securely send data to that server.")
    return True
