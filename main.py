from relay_control import RelayControl

relay_control = RelayControl()

# Triger a specific relay with relay number
relay_control.trigger_relay('127.0.0.1', 5050, relay_number=3, duration=100)

# Trigger All Relays.
relay_control.trigger_relay('127.0.0.1', 5050, duration=100)
