from Crypto.Cipher import Blowfish
from Crypto.Util.Padding import unpad


class Decryptor:

    @staticmethod
    def decrypt_text(encrypted_text: bytes, key: bytes) -> bytes:

        cipher = Blowfish.new(key, Blowfish.MODE_ECB)
        decrypted = cipher.decrypt(encrypted_text)

        return unpad(decrypted, Blowfish.block_size)
