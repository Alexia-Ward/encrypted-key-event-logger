from keyLogging.encryptor import decrypt_data

def view_logs():
    try:
        with open("logs/keylog.enc", "rb") as f:
            for line in f:
                try:
                    decrypted = decrypt_data(line.strip())
                    print(decrypted)
                except:
                    print("Decryption failed for the log entry!")
    except FileNotFoundError:
        print("Log file not found!")

if __name__ == "__main__":
    view_logs()