"""
Code-offset fuzzy extractor.

This module will implement the fuzzy extractor used to derive
stable keys from noisy PUF responses.
"""

def generate_helper_data(response: bytes, key: bytes) -> bytes:
    """Generate helper data for a given PUF response and key."""
    raise NotImplementedError


def reproduce_key(response: bytes, helper_data: bytes) -> bytes:
    """Reproduce the key from a noisy response and helper data."""
    raise NotImplementedError
