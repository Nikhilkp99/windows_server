# test_smb_access.py

import pytest
from services.smb_connector import SMBConnector

OPERATING_SYSTEMS = ['windows', 'linux', 'mac']
SMB_CLIENTS = ['smbclient', 'pySMB', 'WindowsSMB']


@pytest.fixture(params=OPERATING_SYSTEMS, scope='class')
def target_os(request):
    return request.param


@pytest.fixture(params=SMB_CLIENTS, scope='class')
def smb_client(request):
    return request.param


@pytest.fixture(scope='class')
def smb_connector(request, target_os, smb_client):
    connector = SMBConnector(target_os, smb_client)
    # Placeholder for any setup logic
    yield connector
    # Placeholder for any teardown logic
    connector.close()


class TestSMBAccess:

    def test_smb_read(self, smb_connector):
        result = smb_connector.read_from_smb('test_file.txt')
        assert "Reading" in result

    def test_smb_write(self, smb_connector):
        result = smb_connector.write_to_smb('test_file.txt', 'Hello world')
        assert "Writing" in result
