import RPi.GPIO as GPIO
import time
import socket

relay_pins = {
    1: 22,
    2: 24
}

GPIO.setmode(GPIO.BOARD)


def handle_relay(relay_number):
    if relay_number not in relay_pins:
        print(f"Invalid relay number: {relay_number}")
        return

    relay_pin = relay_pins[relay_number]
    print(f"Toggling relay {relay_number} (GPIO {relay_pin})...")

    GPIO.setup(relay_pin, GPIO.OUT)
    GPIO.output(relay_pin, GPIO.LOW)
    time.sleep(0.3)
    GPIO.output(relay_pin, GPIO.HIGH)

    print(f"Relay {relay_number} turned off.")
    GPIO.cleanup(relay_pin)  # Pinleri temizle


HOST = '0.0.0.0'
PORT = 9747

try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

        s.bind((HOST, PORT))
        s.listen()

        print(f"Server started. Listening on {HOST}:{PORT}...")

        while True:
            conn, addr = s.accept()
            with conn:
                print(f"Connection established: {addr}")
                data = conn.recv(1024)
                if data:
                    try:
                        relay_number = int(data.decode())
                        print(f"Received relay number: {relay_number}")
                        handle_relay(relay_number)
                        conn.sendall(b"Relay toggled.")
                    except ValueError:
                        conn.sendall(b"Invalid relay number.")
                else:
                    print("No data received.")
except KeyboardInterrupt:
    print("Shutting down...")
finally:
    GPIO.cleanup()  # GPIO pinlerini temizle
    print("GPIO pins cleaned up.")
