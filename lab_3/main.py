from keygen import SymmetricKey, AsymmetricKey
from encryption import Encryptor
from decryption import Decryptor


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
    SymmetricKey.save_encrypted_symmetric_key(encrypted_symmetric_key,
                                              settings['encrypted_symmetric_key'])

    print("Ключи успешно сгенерированы!")


