import pytest
from services.file_transfer_performance import FileTransferSimulator


class TestFileTransferPerformance:
    @pytest.fixture
    def file_transfer_simulator(self):
        return FileTransferSimulator()

    def test_file_transfer_performance(self, file_transfer_simulator):
        # File size in MB
        file_size = 100

        # Simulate multiple file transfers concurrently
        transfer_speed = 10  # Speed in MB/s
        num_simultaneous_transfers = 5

        # Measure the time taken for each transfer
        transfer_times = [
            file_transfer_simulator.simulate_file_transfer(file_size, transfer_speed)
            for _ in range(num_simultaneous_transfers)
        ]

        # Print the time taken for each transfer
        for i, transfer_time in enumerate(transfer_times):
            print(f"Transfer {i+1}: {transfer_time:.2f} seconds")

        total_time = sum(transfer_times)

        max_acceptable_time = 2 * file_size / transfer_speed

        assert total_time >= max_acceptable_time


if __name__ == "__main__":
    pytest.main(['-v', 'test_performance.py'])
