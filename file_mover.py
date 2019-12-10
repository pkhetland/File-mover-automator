from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(meditek_folder):
            if (
                    "fraktdokumenter" in filename.lower()
                    or "export" in filename.lower()
                    or "servicekort" in filename.lower()
                    or "fraktdokument" in filename.lower()
                    or "shipping" in filename.lower()
                    and filename != 'Servicedokumenter'
            ):
                src = meditek_folder + "/" + filename
                new_destination = folder_destination + "/Servicedokumenter/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif "calc" in filename.lower() or "tilbud" in filename.lower() and filename != 'Tilbud':
                src = meditek_folder + "/" + filename
                new_destination = folder_destination + "/Tilbud/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

        for filename in os.listdir(servicedokumenter_folder):
            if "1219" in filename:
                src = servicedokumenter_folder + "/" + filename
                new_destination = servicedokumenter_folder + "/desember/" + filename.replace(" ", "_")
                os.rename(src, new_destination)


meditek_folder = "/Users/petter/google-drive/Jobb/Meditek"
servicedokumenter_folder = "/Users/petter/google-drive/Jobb/Meditek/Servicedokumenter"
folder_destination = "/Users/petter/google-drive/Jobb/Meditek"

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, meditek_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
