from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


class Encryptor:
    """Performs encryption and decryption operations for the hybrid cryptosystem."""

    @staticmethod
    def encrypt_symmetric_key(sym_key: bytes, public_key) -> bytes:
        """
        Encrypts a symmetric key using the RSA public key.

        :param sym_key: The symmetric key to encrypt.
        :param public_key: The RSA public key.
        :return: The encrypted symmetric key.
        """

        encrypted_key = public_key.encrypt(
            sym_key,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

        return encrypted_key


    @staticmethod
    def decrypt_symmetric_key(encrypted_key: bytes, private_key: RSAPrivateKey) -> bytes:
        """
        Decrypts the symmetric key using the RSA private key.

        :param encrypted_key: The encrypted symmetric key.
        :param private_key: The RSA private key.
        :return: The decrypted symmetric key.
        """

        return private_key.decrypt(
            encrypted_key,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )


    @staticmethod
    def padding(data: bytes) -> bytes:
        """
        Pads the input data before encryption.

        :param data: The data to pad.
        :return: The padded data.
        """

        padder = sym_padding.PKCS7(algorithms.Blowfish.block_size).padder()

        return padder.update(data) + padder.finalize()


    @staticmethod
    def encrypt_text(text: bytes, key: bytes) -> bytes:
        """
        Encrypts plaintext using Blowfish.

        :param text: The plaintext to encrypt.
        :param key: The symmetric key.
        :return: The encrypted ciphertext.
        """

        padded_text = Encryptor.padding(text)
        cipher = Cipher(algorithms.Blowfish(key), modes.ECB())
        encryptor = cipher.encryptor()
        return encryptor.update(padded_text) + encryptor.finalize()
