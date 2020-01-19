from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time


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
                new_destination = meditek_folder + "/Servicedokumenter/" + filename.replace(" ", "_")
                os.rename(src, new_destination)
                print('File has been moved!')
                print(filename)

            elif ("calc" in filename.lower()
                    or "tilbud" in filename.lower()
                    or "offert" in filename.lower()
                    and filename != 'Tilbud'):
                src = meditek_folder + "/" + filename
                new_destination = meditek_folder + "/Tilbud/" + filename.replace(" ", "_")
                os.rename(src, new_destination)
                print('File has been moved!')

            elif ("invoice" in filename.lower()
                    or "signert" in filename.lower()
                    or "faktura" in filename.lower()
                    and filename != 'Fakturaer'):
                src = meditek_folder + "/" + filename
                new_destination = meditek_folder + "/Fakturaer/" + filename.replace(" ", "_")
                os.rename(src, new_destination)
                print('File has been moved!')

        for filename in os.listdir(servicedokumenter_folder):
            if ".pdf" in filename:
                src = servicedokumenter_folder + "/" + filename
                new_destination = servicedokumenter_folder + "/jan/" + filename.replace(" ", "_")
                os.rename(src, new_destination)
                print('File has been moved!')


meditek_folder = "/Users/Petter/google-drive/Jobb/Meditek"
servicedokumenter_folder = "/Users/Petter/google-drive/Jobb/Meditek/Servicedokumenter"

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
