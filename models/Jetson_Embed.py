import socket


class JetsonEmbed:
    def trigger_relays(self, ip, port, relay_number=None, duration=None):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            client.connect((ip, port))
            client.sendall(relay_number.encode())
            print(f"Relay triggered relay number {relay_number}")

            data = client.recv(1024)
            print(f"Response: {data.decode()}")
            return True
