from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import os
import json
import time
import shutil


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(downloads_folder):
            if filename.endswith(('.dmg')):
                src = downloads_folder + "/" + filename
                new_destination = dmg_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.xlsx', '.csv')):
                src = downloads_folder + "/" + filename
                new_destination = excel_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.jpg', '.jpeg', '.png')):
                src = downloads_folder + "/" + filename
                new_destination = img_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.pptx', '.ppt')):
                src = downloads_folder + "/" + filename
                new_destination = powerpoint_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.pdf')):
                src = downloads_folder + "/" + filename
                new_destination = pdf_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.zip')):
                src = downloads_folder + "/" + filename
                new_destination = zip_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)

            elif filename.endswith(('.docx', '.doc')):
                src = downloads_folder + "/" + filename
                new_destination = docs_folder + "/" + filename.replace(" ", "_")
                os.rename(src, new_destination)



downloads_folder = "/Users/Petter/Downloads"
img_folder = "/Users/Petter/Downloads/img"
pdf_folder = "/Users/Petter/Downloads/pdf"
powerpoint_folder = "/Users/Petter/Downloads/powerpoint"
dmg_folder = "/Users/Petter/Downloads/dmg"
zip_folder = "/Users/Petter/Downloads/zip"
excel_folder = "/Users/Petter/Downloads/excel"
docs_folder = "/Users/Petter/Downloads/docs"

event_handler = MyHandler()

observer = Observer()
observer.schedule(event_handler, downloads_folder, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
