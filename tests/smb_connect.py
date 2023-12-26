from smb.SMBConnection import SMBConnection

# Replace these values with your SMB server details
smb_host = 'WIN-HAMMER'
smb_port = 139  # Default port for SMB version 1.0
smb_user = 'msys'
smb_password = 'Master#123456'
smb_domain = 'WORKGROUP'
shared_folder_path = '\\\\WIN-HAMMER\\sharedSMB'

# Create an SMB connection
conn = SMBConnection(smb_user, smb_password, 'pytest-client', smb_host, smb_domain, use_ntlm_v2=True)

# Establish the connection
if not conn.connect(smb_host, smb_port):
    print("Failed to connect to SMB server")
else:
    try:
        # List files in the shared folder
        files = conn.listPath(shared_folder_path, '/')

        # Display the list of files
        for file in files:
            print(file.filename)
    except Exception as e:
        print(f"Error accessing shared folder: {e}")
    finally:
        # Close the connection
        conn.close()
