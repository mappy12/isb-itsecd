from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding as rsa_padding
from cryptography.hazmat.primitives.asymmetric.rsa import RSAPrivateKey


class Encryptor:

    @staticmethod
    def encrypt_symmetric_key(sym_key: bytes, public_key) -> bytes:

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
        padder = sym_padding.PKCS7(algorithms.Blowfish.block_size).padder()

        return padder.update(data) + padder.finalize()


    @staticmethod
    def encrypt_text(text: bytes, key: bytes) -> bytes:

        padded_text = Encryptor.padding(text)
        cipher = Cipher(algorithms.Blowfish(key), modes.ECB())
        encryptor = cipher.encryptor()
        return encryptor.update(padded_text) + encryptor.finalize()
