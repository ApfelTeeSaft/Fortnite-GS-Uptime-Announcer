import time
import pygetwindow as gw
import pyautogui
import requests
from datetime import datetime
from os import system

system("title " + "Server Uptime Announcer")
print("made with love by apfelteesaft\nmy github: https://github.com/apfelteesaft \n")

def is_window_open(window_name):
    return bool(gw.getWindowsWithTitle(window_name))

def wait_for_window_to_close(window_name):
    while is_window_open(window_name):
        print(f"Waiting for Gameserver to restart...")
        time.sleep(10)

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

#adjust these settings to your infos
startup_delay = 65 # the ammount of time in seconds it takes for your gameserver to be joinable (from when the window opens)
webhook_url = "your_webhook_url_here" # the webhook url for your discord webhook
gameserver_name = "Project Reboot" # leave this to "Project Reboot" if you are using the Reboot GS, otherwise the name of the gameserver is the window title! (for example, this is a window title: https://media.discordapp.net/attachments/1154892615901270188/1164148536691142727/image.png?ex=654228cf&is=652fb3cf&hm=87f558780ad41b14f83599e170ce93b9315db9b01295d54ec463a247b142b1a7&=&width=968&height=30)

data = {
    "embeds": [
        {
            "title": "Server Up!",
            "description": "The Gameserver is Ready, Ready up to Play!",
            "color": 65280,  # Green color (0x00FF00)
            "footer": {
                "text": f"Posted at {current_time}"
            }
        }
    ]
}
if __name__ == "__main__":
    target_window_name = gameserver_name

    while True:
        if is_window_open(target_window_name):
            print(f"Waiting for {startup_delay} seconds so that the Gameserver Starts correctly!") # waiting for the gameserver to start correctly and then posts the message to the webhook
            time.sleep(startup_delay)
            response = requests.post(webhook_url, json=data)
            print("Sent Message to Webhook!")
            wait_for_window_to_close(target_window_name) # when gameserver closes, it enters a loop where it waits for the gameserver to start again
        else:
            print("Waiting for the process...")
            time.sleep(10)