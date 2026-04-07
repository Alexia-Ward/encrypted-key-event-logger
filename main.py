# Output menu to choose between logging keystrokes or viewing logs
choice = input("Choose mode: (1) Log keystrokes, (2) View logs, (3) Exit: ")

#Import and run the appropriate function based on user input 
if choice == "1":
    from keyLogging.logger import start
    start()
elif choice == "2":
    from viewer import view_logs
    view_logs()   
elif choice == "3":
    print("Exiting the program. Thank you for using the keylogger!") 
else:
    print("Invalid choice! Please enter 1, 2, or 3!")  