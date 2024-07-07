# Multiple processes using os.fork module
import os
import subprocess

def ping(host):
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if result.returncode == 0:
        print('%s: up' % host)
    else:
        print('%s: down' % host)

def get_ip_range(network_base, start, end):
    return ['%s.%s' % (network_base, i) for i in range(start, end + 1)]

if __name__ == '__main__':
    network = input("Enter the network base (e.g., 192.168.0): ")
    start_ip = int(input("Enter the start of the IP range: "))
    end_ip = int(input("Enter the end of the IP range: "))

    ips = get_ip_range(network, start_ip, end_ip)

    for ip in ips:
        pid = os.fork()
        if pid == 0:
            # Child process
            ping(ip)
            os._exit(0)  # Ensure child process exits after pinging
        elif pid > 0:
            # Parent process
            continue
        else:
            print("Fork failed!")

    # Wait for all child processes to complete
    for _ in ips:
        os.wait()


# Multiple threads using threading module
import os
import threading

def ping(host):
    result = subprocess.run(
        'ping -c2 %s &> /dev/null' % host, shell=True
    )
    if result.returncode == 0:
        print('%s: up' % host)
    else:
        print('%s: down' % host)

def get_ip_range(network_base, start, end):
    return ['%s.%s' % (network_base, i) for i in range(start, end + 1)]

if __name__ == '__main__':
    network = input("Enter the network base (e.g., 192.168.0): ")
    start_ip = int(input("Enter the start of the IP range: "))
    end_ip = int(input("Enter the end of the IP range: "))

    ips = get_ip_range(network, start_ip, end_ip)
    for ip in ips:
            t = threading.Thread(target=ping, args=(ip, ))
            t.start()
