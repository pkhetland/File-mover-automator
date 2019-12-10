from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


import os
import json
import time

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            if "1219" in filename.lower() or "servicekort" in filename.lower():
                src = folder_to_track + "/" + filename
                new_destination = folder_destination + "/" + filename
                os.rename(src, new_destination)


folder_to_track = "/users/petter/google-drive/Jobb/Meditek"
folder_destination = "/users/petter/google-drive/Jobb/Meditek/A-Servicedokumenter-Desember"

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except(KeyboardInterrupt):
    observer.stop()
observer.join()
