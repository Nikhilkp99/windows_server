import shutil
import os


class FileSystemBackupRestore:
    def __init__(self, backup_directory):
        self.backup_directory = backup_directory

    def perform_backup(self, source_file):
        # Create the backup directory if it doesn't exist
        os.makedirs(self.backup_directory, exist_ok=True)

        # Generate a backup file path
        backup_file = os.path.join(self.backup_directory, f"backup_{os.path.basename(source_file)}")

        # Perform the backup (copy the file to the backup directory)
        shutil.copy(source_file, backup_file)

        return backup_file

    def perform_restore(self, backup_file, destination_directory):
        # Generate the restore file path
        restored_file = os.path.join(destination_directory, f"restored_{os.path.basename(backup_file)}")

        # Perform the restore (move the file back to the original location)
        shutil.move(backup_file, restored_file)

        return restored_file
