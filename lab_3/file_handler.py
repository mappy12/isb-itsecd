import json


class FileHandler:

    @staticmethod
    def save_encrypted_symmetric_key(encrypted_key: bytes, path: str) -> None:
        """
        Saves encrypted symmetric key to a file.

        :param encrypted_key: The encrypted symmetric key.
        :param path: Destination file path.
        :return:
        """

        with open(path, "wb") as file:
            file.write(encrypted_key)


    @staticmethod
    def read_file(filename: str) -> bytes:
        """
        Reads data from a file.

        :param filename: Path to the file.
        :return: File contents.
        """

        with open(filename, "rb") as file:
            return file.read()


    def write_to_file(filename: str, data: bytes) -> None:
        """
        Writes data to a file.

        :param data: Path to the file.
        :return: Data to write.
        """

        with open(filename, 'wb') as f:
            f.write(data)


    @staticmethod
    def load_settings(filename: str) -> dict:
        """
        Loads settings from a JSON file.

        :param filename: Path to the JSON settings file.
        :return: Settings dictionary.
        """

        with open(filename, 'r') as f:
            return json.load(f)
