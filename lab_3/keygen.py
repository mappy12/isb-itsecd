import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

class SymmetricEncryption:

    @staticmethod
    def generate_sym_key(key_length: int) -> bytes:

        if key_length < 32 or key_length > 448 or key_length % 8 != 0:
            raise ValueError("Blowfish key length must be between 32 and 448 bits, in 8-bit steps.")

        key = os.urandom(key_length // 8)

        return key


class AssymetricEncryption:

    @staticmethod
    def generate_assym_key() -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        return private_key, public_key
