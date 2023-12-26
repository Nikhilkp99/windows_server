from cryptography.fernet import Fernet


class CryptoHandler:
    def __init__(self, key):
        self.key = key
        self.cipher = Fernet(self.key)

    def encrypt_data(self, data):
        encrypted_data = self.cipher.encrypt(data.encode())
        return encrypted_data

    def decrypt_data(self, encrypted_data):
        decrypted_data = self.cipher.decrypt(encrypted_data).decode()
        return decrypted_data
