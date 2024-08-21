import socket
from models.Rl02_IO import Rl02IO
from models.Rn62_IO import Rn62IO


class RelayControl:
    def __init__(self, brand):
        self.brand = brand

        if self.brand == 'rl-02':
            self.relay_instance = Rl02IO()
        elif self.brand == 'rn-62':
            self.relay_instance = Rn62IO()
        else:
            raise ValueError("Unsupported brand for relay control")

    def trigger_relay(self, ip, port, relay_number=None, duration=100):
        return self.relay_instance.trigger_relays(ip, port, relay_number, duration)
