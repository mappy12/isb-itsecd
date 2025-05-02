import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

class SymmetricKey:

    @staticmethod
    def get_key_length() -> int:

        while True:

            try:

                key_length = int(input("Введите длину симметричного ключа: "))

                if key_length < 32 or key_length > 448 or key_length % 8 != 0:
                    print("Blowfish key length must be between 32 and 448 bits, in 8-bit steps.")

                else:
                    return key_length

            except ValueError:

                print("Ошибка: введите целое число!")


    @staticmethod
    def generate_sym_key(key_length: int) -> bytes:

        key = os.urandom(key_length // 8)
        return key


    @staticmethod
    def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:

        with open(path, "wb") as file:
            file.write(encrypted_key)



class AsymmetricKey:

    @staticmethod
    def generate_assym_key() -> tuple:
        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        return private_key, public_key


    @staticmethod
    def serialize_private_key(private_key: rsa.RSAPrivateKey, filepath: str) -> None:
        with open(filepath, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )


    @staticmethod
    def serialize_public_key(public_key: rsa.RSAPublicKey, filepath: str) -> None:
        with open(filepath, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )

    @staticmethod
    def load_private_key(path: str) -> RSAPrivateKey:
        with open(path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        return private_key


    @staticmethod
    def load_encrypted_symmetric_key(path: str) -> bytes:
        with open(path, "rb") as f:
            return f.read()
