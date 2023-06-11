import subprocess
import os


def basic_download(url, save_path):
    # wget -c -P ~/Downloads/ "https://domain.com/item"
    subprocess.run(
        ["wget", "-c", "-P", save_path, url]
    )
