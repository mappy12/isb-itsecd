import os

from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import pad
from cryptography.hazmat.primitives import serialization, hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


class Encryptor:

    @staticmethod
    def read_text(filename: str) -> bytes:
        with open(filename, "rb") as file:
            return file.read()


    @staticmethod
    def decrypt_symmetric_key(encrypted_key: bytes, private_key: RSAPrivateKey) -> bytes:
        return private_key.decrypt(
            encrypted_key,
            rsa_padding.OAEP(
                mgf=rsa_padding.MGF1(algorithm=hashes.SHA256()),
                algorithm=hashes.SHA256(),
                label=None
            )
        )

    @staticmethod
    def padding(data: bytes):
        return pad(data, Blowfish.block_size)


    @staticmethod
    def encrypt_text(text: bytes, key: bytes) -> bytes:

        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        padded_text = Encryptor.padding(text)
        cipher_text = cipher.encrypt(padded_text)

        return cipher_text



