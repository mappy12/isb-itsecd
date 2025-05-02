from cryptography.hazmat.primitives import padding as sym_padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes


class Decryptor:

    @staticmethod
    def unpadding(padded_data: bytes) -> bytes:
        """
        Removes padding from decrypted text.

        :param padded_data: Decrypted text with padding.
        :return: Original unpadded text.
        """

        unpadder = sym_padding.PKCS7(algorithms.Blowfish.block_size).unpadder()
        return unpadder.update(padded_data) + unpadder.finalize()


    @staticmethod
    def decrypt_text(encrypted_text: bytes, key: bytes) -> bytes:
        """
        Decrypts text using the Blowfish algorithm.

        :param encrypted_text: The encrypted text.
        :param key: The symmetric key.
        :return: Decrypted and unpadded plaintext.
        """

        cipher = Cipher(algorithms.Blowfish(key), modes.ECB())
        decryptor = cipher.decryptor()
        decrypted_padded = decryptor.update(encrypted_text) + decryptor.finalize()
        return Decryptor.unpadding(decrypted_padded)
