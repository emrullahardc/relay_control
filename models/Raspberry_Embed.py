import socket


class RaspberryEmbed:
    def trigger_relays(self, ip, port, relay_number=None, duration=None):
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
                client.connect((ip, port))

                if relay_number is not None:
                    command = f"{relay_number},{duration}".encode() if duration else str(relay_number).encode()
                    client.sendall(command)

                    print(
                        f"Relay triggered: relay number {relay_number} for duration {duration} seconds" if duration else f"Relay triggered: relay number {relay_number}")

                    data = client.recv(1024)
                    print(f"Response: {data.decode()}")
                else:
                    print("No relay number provided.")

                return True
        except socket.error as e:
            print(f"Socket error occurred: {e}")
            return False
