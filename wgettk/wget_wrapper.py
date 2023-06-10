import subprocess
import os


def basic_download(url):
    # wget -c -P ~/Downloads/ "https://domain.com/item"
    subprocess.run(
        ["wget", "-c", "-P", os.path.expanduser("~/Downloads/"), self.url.get()]
    )
