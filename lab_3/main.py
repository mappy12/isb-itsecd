from os import write

from Crypto.SelfTest.Protocol.test_ecdh import private_key

from keygen import SymmetricKey, AsymmetricKey
from encryption import Encryptor
from decryption import Decryptor
from lab_3.file_handler import FileHandler


def genereate_keys(settings):

    print("====Режим генерации ключей====")

    key_length = SymmetricKey.get_key_length()
    sym_key = SymmetricKey.generate_sym_key(key_length)
    print("Симметричный ключ успешно сгененрирован.")

    private_key, public_key = AsymmetricKey.generate_assym_key()
    print("Асимметричная пара ключей успешно сгенерирована.")

    AsymmetricKey.serialize_private_key(private_key, settings['private_key'])
    AsymmetricKey.serialize_public_key(public_key, settings['public_key'])

    encrypted_symmetric_key = Encryptor.encrypt_symmetric_key(sym_key, public_key)
    FileHandler.save_encrypted_symmetric_key(encrypted_symmetric_key,
                                              settings['encrypted_symmetric_key'])

    print("Ключи успешно сгенерированы!")


def encrypt_mode(settings):

    encrypted_symmetric_key = AsymmetricKey.load_encrypted_symmetric_key(
        settings['encrypted_symmetric_key'])
    private_key = AsymmetricKey.load_private_key(settings['private_key'])
    symmetric_key = Encryptor.decrypt_symmetric_key(encrypted_symmetric_key, private_key)

    text = FileHandler.read_file(settings['plaintext'])
    encrypted_text = Encryptor.encrypt_text(text, symmetric_key)

    FileHandler.write_to_file(settings['encrypted_text'], encrypted_text)

    print("Текст был успешно зашифрован и сохранен в файл!")


def decrypt_mode(settings):

    encrypted_symmetric_key = AsymmetricKey.load_encrypted_symmetric_key(
        settings['encrypted_symmetric_key'])
    private_key = AsymmetricKey.load_private_key(settings['private_key'])

    symmetric_key = Encryptor.decrypt_symmetric_key(encrypted_symmetric_key, private_key)
    encrypted_text = FileHandler.read_file(settings['encrypted_text'])

    decrypted_text = Decryptor.decrypt_text(encrypted_text, symmetric_key)
    FileHandler.write_to_file(settings['decrypted_text'], decrypted_text)

    print("Текст был успешно зашифровал и сохранен в файл!")
