import time
import pygetwindow as gw
import pyautogui
import requests
from datetime import datetime
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)
startup_delay = os.environ.get("time")
webhook_url = os.environ.get("webhook_url")
gameserver_name = os.environ.get("gameserver_name")

os.system("title " + "Server Uptime Announcer")
print("made with love by apfelteesaft\nmy github: https://github.com/apfelteesaft \n")

def is_window_open(window_name):
    return bool(gw.getWindowsWithTitle(window_name))

def wait_for_window_to_close(window_name):
    while is_window_open(window_name):
        print(f"Waiting for Gameserver to restart...")
        time.sleep(10)

current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

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
            print(gameserver_name)
            time.sleep(10)