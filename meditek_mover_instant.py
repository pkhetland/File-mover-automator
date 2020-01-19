import os
import json
import time

meditek_folder = "/Users/Petter/google-drive/Jobb/Meditek"
servicedokumenter_folder = "/Users/Petter/google-drive/Jobb/Meditek/servicedokumenter"
jan_folder = "/Users/Petter/google-drive/Jobb/Meditek/servicedokumenter/jan"
fakturaer_folder = "/Users/Petter/google-drive/Jobb/Meditek/fakturaer"
media_folder = "/Users/Petter/google-drive/Jobb/Meditek/media"

def files(path):
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            yield file

if __name__ == "__main__":

    moved_files = 0

    for filename in files(meditek_folder):
        if (
                "fraktdokumenter" in filename.lower()
                or "export" in filename.lower()
                or "servicekort" in filename.lower()
                or "fraktdokument" in filename.lower()
                or "shipping" in filename.lower()
            ):
            src = meditek_folder + "/" + filename
            new_destination = meditek_folder + "/servicedokumenter/" + filename.replace(" ", "_")
            os.rename(src, new_destination)
            moved_files += 1

        elif (
                "calc" in filename.lower()
                or "tilbud" in filename.lower()
                or "offert" in filename.lower()
            ):
            src = meditek_folder + "/" + filename
            new_destination = meditek_folder + "/kundetilbud/" + filename.replace(" ", "_")
            os.rename(src, new_destination)
            moved_files += 1

        elif ("invoice" in filename.lower()
                or "signert" in filename.lower()
                or "faktura" in filename.lower()
        ):
            src = meditek_folder + "/" + filename
            new_destination = meditek_folder + "/fakturaer/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1

    for filename in files(servicedokumenter_folder):
        if "0120" in filename:
            src = servicedokumenter_folder + "/" + filename
            new_destination = servicedokumenter_folder + "/jan/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1

    for filename in files(jan_folder):
        if "servicekort" in filename.lower():
            src = jan_folder + "/" + filename
            new_destination = jan_folder + "/servicekort_jan/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1
        elif (
            "fraktdokumenter" in filename.lower()
            or "export" in filename.lower()
            or "fraktdokument" in filename.lower()
            or "shipping" in filename.lower()
        ):
            src = jan_folder + "/" + filename
            new_destination = jan_folder + "/fraktdokumenter_jan/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1

    """ FAKTURAER """
    for filename in files(fakturaer_folder):
        if "signert" in filename.lower() or "signed" in filename.lower():
            src = fakturaer_folder + "/" + filename
            new_destination = fakturaer_folder + "/signerte_fakturaer/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1
        elif "steris" in filename.lower():
            src = fakturaer_folder + "/" + filename
            new_destination = fakturaer_folder + "/steris/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1
        elif "invoice" in filename.lower() or "faktura" in filename.lower():
            src = fakturaer_folder + "/" + filename
            new_destination = fakturaer_folder + "/andre_fakturaer/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1
        
    """ MEDIA """    
    for filename in files(meditek_folder):
        if (
            ".jpeg" in filename.lower()
            or ".png" in filename.lower()
            or ".svg" in filename.lower()
            or ".jpg" in filename.lower()
        ):
            src = meditek_folder + "/" + filename
            new_destination = media_folder + "/" + filename.replace(" ", "_").lower()
            os.rename(src, new_destination)
            moved_files += 1
    if moved_files > 0:
        print(f'Suksess! Antall filer flyttet: {moved_files}')
    else:
        print('Ingen filer ble flyttet!')