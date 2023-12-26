import os
import shutil
import threading
import pytest
from services.share_acess import FileOperations


class TestConcurrentFileAccess:
    test_directory = None

    @classmethod
    def setup_class(cls):
        cls.test_directory = "D:\\Shared_Access"
        cls.cleanup_test_directory()  # directory is cleaned up
        os.makedirs(cls.test_directory)

    @classmethod
    def teardown_class(cls):
        cls.cleanup_test_directory()

    @classmethod
    def cleanup_test_directory(cls):
        # Remove the directory if it exists.
        if cls.test_directory and os.path.exists(cls.test_directory):
            shutil.rmtree(cls.test_directory)

    def test_concurrent_read(self):
        file_ops = FileOperations(base_path=self.test_directory)
        file_path = os.path.join(self.test_directory, "shared_file.txt")
        file_ops.write_file(file_path, "Initial content")

        def read_file_task():
            content = file_ops.read_file(file_path)
            assert content == "Initial content"

        thread1 = threading.Thread(target=read_file_task)
        thread2 = threading.Thread(target=read_file_task)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

    def test_concurrent_write(self):
        file_ops = FileOperations(base_path=self.test_directory)
        file_path = os.path.join(self.test_directory, "shared_file.txt")

        # Remove the file if it already exists
        if os.path.exists(file_path):
            os.remove(file_path)

        def write_file_task():
            file_ops.write_file(file_path, "Content from Thread 1")

        def write_file_task_2():
            file_ops.write_file(file_path, "Content from Thread 2")

        thread1 = threading.Thread(target=write_file_task)
        thread2 = threading.Thread(target=write_file_task_2)

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        final_content = file_ops.read_file(file_path)
        assert final_content == "Content from Thread 2" or final_content == ""


if __name__ == "__main__":
    pytest.main()
