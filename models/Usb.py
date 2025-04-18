import os


class Usb:
    HIDRAW_PATHS = {
        1: "/dev/hidraw0",
        2: "/dev/hidraw1",
    }

    COMMANDS = {
        "open": bytes([0xA0, 0x01, 0x01, 0xA2]),
        "close": bytes([0xA0, 0x01, 0x00, 0xA1]),
    }

    def trigger_relays(self, device_index: int, state: str, duration = None):
        if state not in self.COMMANDS:
            raise ValueError("State must be 'open' or 'close'")
        if device_index not in self.HIDRAW_PATHS:
            raise ValueError(f"Invalid device index: {device_index}")

        command = self.COMMANDS[state]
        path = self.HIDRAW_PATHS[device_index]

        try:
            with open(path, "wb") as device:
                device.write(command)
            print(f"Relay {state} command sent to {path} successfully.")
            return True
        except Exception as e:
            print(f"Error sending command to {path}: {e}")
            return False
