import os
import pytest
from services.file_folder_operations import FileFolderOperations


@pytest.fixture
def file_folder_operations():
    # Setup: Create an instance of the FileFolderOperations class
    base_path = 'D:\\Myfolder'
    file_folder_ops = FileFolderOperations(base_path=base_path)
    yield file_folder_ops


class TestFileFolderOperations:

    def test_create_file(self, file_folder_operations):
        file_folder_operations.create_file('test_file.txt')
        assert os.path.isfile(os.path.join(file_folder_operations.base_path, 'test_file.txt'))

    def test_modify_file(self, file_folder_operations):
        file_folder_operations.create_file('test_file.txt', 'Initial content')
        file_folder_operations.modify_file('test_file.txt', 'New content')
        with open(os.path.join(file_folder_operations.base_path, 'test_file.txt'), 'r') as f:
            assert f.read() == 'New content'

    def test_delete_file(self, file_folder_operations):
        file_folder_operations.delete_file('test_file.txt')
        assert not os.path.exists(os.path.join(file_folder_operations.base_path, 'test_file.txt'))

    def test_create_folder(self, file_folder_operations):
        file_folder_operations.create_folder('test_folder')
        assert os.path.isdir(os.path.join(file_folder_operations.base_path, 'test_directory', 'test_folder'))

    def test_delete_folder(self, file_folder_operations):
        file_folder_operations.delete_folder('test_folder')
        assert not os.path.exists(os.path.join(file_folder_operations.base_path, 'test_directory', 'test_folder'))


