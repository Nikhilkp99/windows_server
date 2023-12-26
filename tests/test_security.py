import pytest
from cryptography.fernet import Fernet

from services.encryption_mod import CryptoHandler


class TestCryptoHandler:
    @pytest.fixture
    def crypto_handler(self):
        key = Fernet.generate_key()
        return CryptoHandler(key)

    def test_encrypt_decrypt(self, crypto_handler):
        original_data = "Hello, this is a secret message!"

        encrypted_data = crypto_handler.encrypt_data(original_data)
        # print(f"Encrypted Data: {encrypted_data}")

        decrypted_data = crypto_handler.decrypt_data(encrypted_data)

        assert decrypted_data == original_data


if __name__ == "__main__":
    pytest.main(['-v', 'test_encryption.py'])
