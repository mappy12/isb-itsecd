import os

class SymmetricEncryption:

    @staticmethod
    def generate_sym_key(key_length: int) -> bytes:

        if key_length < 32 or key_length > 448 or key_length % 8 != 0:
            raise ValueError("Blowfish key length must be between 32 and 448 bits, in 8-bit steps.")

        key = os.urandom(key_length // 8)

        return key

