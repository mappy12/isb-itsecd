import json
import os


class FileHandler:

    @staticmethod
    def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:

        with open(path, "wb") as file:
            file.write(encrypted_key)


    @staticmethod
    def read_file(filename: str) -> bytes:

        with open(filename, "rb") as file:
            return file.read()


    def write_to_file(filename: str, data: bytes) -> None:

        with open(filename, 'wb') as f:
            f.write(data)


    @staticmethod
    def load_settings(filename: str) -> dict:
        with open(filename, 'r') as f:
            return json.load(f)
