import os

from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey

class SymmetricKey:
    """Handles generation of symmetric keys for Blowfish encryption."""

    @staticmethod
    def get_key_length() -> int:
        """
        Prompts the user to input a valid Blowfish key length.

        :return: A valid key length between 32 and 448 bits (inclusive), divisible by 8.
        """

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
        """
        Generates a random symmetric key of the given length.

        :param key_length: The key length
        :return: The generated symmetric key.
        """

        key = os.urandom(key_length // 8)
        return key


class AsymmetricKey:
    """Handles generation, serialization, and loading of RSA asymmetric key pairs."""

    @staticmethod
    def generate_assym_key() -> tuple:
        """
        Generates an RSA private/public key pair.

        :return: (private_key, public_key) as RSA key objects.
        """

        private_key = rsa.generate_private_key(
            public_exponent=65537,
            key_size=2048,
            backend=default_backend()
        )

        public_key = private_key.public_key()

        return private_key, public_key


    @staticmethod
    def serialize_private_key(private_key: rsa.RSAPrivateKey, filename: str) -> None:
        """
        Serializes and saves the RSA private key

        :param private_key: The private key
        :param filename: The path where the key should be saved.
        :return: None
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "wb") as f:
            f.write(
                private_key.private_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PrivateFormat.TraditionalOpenSSL,
                    encryption_algorithm=serialization.NoEncryption()
                )
            )


    @staticmethod
    def serialize_public_key(public_key: rsa.RSAPublicKey, filename: str) -> None:
        """
        Serializes and saves the RSA public key

        :param public_key: The public key
        :param filename: The path where the key should be saved.
        :return:
        """

        os.makedirs(os.path.dirname(filename), exist_ok=True)

        with open(filename, "wb") as f:
            f.write(
                public_key.public_bytes(
                    encoding=serialization.Encoding.PEM,
                    format=serialization.PublicFormat.SubjectPublicKeyInfo
                )
            )


    @staticmethod
    def load_private_key(path: str) -> RSAPrivateKey:
        """
        Loads an RSA private key from a  file.

        :param path: Path to the private key file.
        :return: The loaded private key.
        """

        with open(path, "rb") as f:
            private_key = serialization.load_pem_private_key(
                f.read(),
                password=None
            )
        return private_key


    @staticmethod
    def load_encrypted_symmetric_key(path: str) -> bytes:
        """
        Loads an encrypted symmetric key from a file.

        :param path: Path to the encrypted symmetric key file.
        :return: The encrypted symmetric key.
        """

        with open(path, "rb") as f:
            return f.read()
