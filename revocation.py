"""
Signed revocation lists.
"""

def create_revocation_list(revoked_ids: list[bytes], signing_key) -> bytes:
    """Create a signed revocation list."""
    raise NotImplementedError


def is_revoked(device_id: bytes, revocation_list: bytes, public_key) -> bool:
    """Check whether a device identifier is revoked."""
    raise NotImplementedError
