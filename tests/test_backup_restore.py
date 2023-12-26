import pytest
import tempfile
import os
from services.backup_restore import FileSystemBackupRestore


class TestFileSystemBackupRestore:
    @pytest.fixture
    def backup_restore_instance(self):
        # Use a temporary directory for testing
        temp_dir = tempfile.mkdtemp()
        return FileSystemBackupRestore(temp_dir)

    def test_backup_and_restore(self, backup_restore_instance):
        # Data to be backed up
        source_file = "test_data.txt"
        with open(source_file, "w") as file:
            file.write("Gladson,anil,manish")

        # Perform backup
        backup_file = backup_restore_instance.perform_backup(source_file)

        # Perform restore
        restored_file = backup_restore_instance.perform_restore(backup_file, os.getcwd())

        # Assert that the restored file content matches the original data
        with open(restored_file, "r") as file:
            restored_data = file.read()

        original_data = "Gladson,anil,manish"
        assert restored_data == original_data


if __name__ == "__main__":
    pytest.main(['-v', 'test_filesystem_backup_restore.py'])
