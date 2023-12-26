import os
import shutil

class FileFolderOperations:
    def __init__(self, base_path='D:\\Myfolder'):
        self.base_path = base_path

    def create_file(self, file_name, content=''):
        file_path = os.path.join(self.base_path, file_name)
        try:
            with open(file_path, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error creating file {file_name}: {e}")

    def modify_file(self, file_name, content):
        file_path = os.path.join(self.base_path, file_name)
        try:
            with open(file_path, 'w') as f:
                f.write(content)
        except Exception as e:
            print(f"Error modifying file {file_name}: {e}")

    def delete_file(self, file_name):
        file_path = os.path.join(self.base_path, file_name)
        try:
            os.remove(file_path)
        except Exception as e:
            print(f"Error deleting file {file_name}: {e}")

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.base_path, 'test_directory', folder_name)
        try:
            os.makedirs(folder_path, exist_ok=True)
        except Exception as e:
            print(f"Error creating folder {folder_name}: {e}")

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.base_path, 'test_directory', folder_name)
        try:
            shutil.rmtree(folder_path)
        except Exception as e:
            print(f"Error deleting folder {folder_name}: {e}")

    def check_permissions(self, file_name):
        file_path = os.path.join(self.base_path, file_name)
        # Implement your logic to check permissions and return them
        # This can vary based on the platform and the way permissions are represented
