"""
Hash-chain token scheme (Lamport / TESLA-style).

Used to create compact authentication tokens suitable for
very low-bandwidth links.
"""

def generate_chain(seed: bytes, length: int) -> list[bytes]:
    """Generate a hash chain of the given length."""
    raise NotImplementedError


def verify_token(token: bytes, commitment: bytes, index: int) -> bool:
    """Verify a token against a commitment."""
    raise NotImplementedError
