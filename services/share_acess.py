import os


class FileOperations:
    def __init__(self, base_path="."):
        self.base_path = base_path

    def read_file(self, file_name):
        """Read the contents of a file."""
        file_path = os.path.join(self.base_path, file_name)
        with open(file_path, 'r') as file:
            content = file.read()
        return content

    def write_file(self, file_name, content):
        """Write content to a file."""
        file_path = os.path.join(self.base_path, file_name)
        with open(file_path, 'w') as file:
            file.write(content)
