import time


class FileTransferSimulator:
    @staticmethod
    def simulate_file_transfer(file_size, transfer_speed):
        transfer_time = file_size / transfer_speed
        time.sleep(transfer_time)
        return transfer_time
