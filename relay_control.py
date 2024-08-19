import socket


class RelayControl:
    def __init__(self):
        self.RELAY_BEGIN_COMMAND = '<RL_BEGIN>'
        self.RELAY_END_COMMAND = '</RL_END>'
        self.RELAY_COUNT = 16

    def trigger_relay(self, ip, port, relay_number=None, duration=100):
        commands = [self.RELAY_BEGIN_COMMAND]

        if relay_number is None:
            for i in range(self.RELAY_COUNT):
                relay_command = f'<RL{i}>{duration}</RL{i}>'
                commands.append(relay_command)
        else:
            if relay_number < 0 or relay_number >= self.RELAY_COUNT:
                raise ValueError("Relay number must be between 0 and 15.")
            relay_command = f'<RL{relay_number}>{duration}</RL{relay_number}>'
            commands.append(relay_command)

        commands.append(self.RELAY_END_COMMAND)
        data_to_send = ''.join(commands)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
            try:
                client.connect((ip, port))
                client.sendall(data_to_send.encode('ascii'))
                print(f"Command sent: {data_to_send}")

                response = client.recv(1024).decode('ascii')
                print(f"Received data: {response}")
            except Exception as e:
                print(f"Failed to send relay command: {e}")
