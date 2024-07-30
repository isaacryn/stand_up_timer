import os
from time import sleep
import subprocess

filename = "stand_up_reminder.txt"
message = "Stand the fuck up!"


def create_and_open_reminder_file(filename, message):
    if not os.path.exists(filename):
        with open(filename, 'w') as file:
            file.write(message)

    applescript = f'''
    set file_path to POSIX file "{os.path.abspath(filename)}"
    tell application "TextEdit"
        open file_path
        activate
    end tell
    delay 3
    tell application "TextEdit"
        close front window
    end tell
    '''

    # Run the AppleScript to open the file in TextEdit and close it after 3 seconds
    subprocess.run(['osascript', '-e', applescript])

    # Check if TextEdit is running
    while True:
        # Use AppleScript to check if TextEdit is running
        check_textedit_script = '''
        tell application "System Events"
            exists process "TextEdit"
        end tell
        '''
        result = subprocess.run(['osascript', '-e', check_textedit_script], capture_output=True, text=True)

        # If TextEdit is not running, break the loop
        if "false" in result.stdout:
            break

        # Delay for a short period before checking again
        sleep(1)


def notify(title, message):
    # Assuming pync.notify is used for notification, though not used in this script
    pass


def stand_up():
    while True:
        sleep(3)
        create_and_open_reminder_file(filename, message)
        print("Stand the fuck up")
