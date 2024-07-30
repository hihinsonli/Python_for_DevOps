import paramiko
import atexit

# Define SSH details
hostname = 'hostname'
username = 'username'
private_key_path = '/path/to/private/key/id_rsa'

# Load the private key
private_key = paramiko.RSAKey.from_private_key_file(private_key_path)

# Create SSH client instance
client = paramiko.SSHClient()
client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

# Register cleanup function to close the client on exit
def cleanup():
    client.close()

atexit.register(cleanup)

# Connect to the server
client.connect(hostname, username=username, pkey=private_key)

# Execute a command
command = 'mkdir -p /root/paramiko_folder'
stdin, stdout, stderr = client.exec_command(command)

# Print errors if any
error = stderr.read().decode()
if error:
    print(f"Error: {error}")
