import logging
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
import subprocess
import os

logger = logging.getLogger(__name__)
# set logging level for ENTIRE logger
logger.setLevel(logging.DEBUG)
# create console handler and set level to debug
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
# create formatter
formatter = logging.Formatter(
    "%(asctime)s - %(filename)s:%(funcName)s - %(levelname)s - %(message)s"
)
# add formatter to chINFO
ch.setFormatter(formatter)
# add ch to logger
logger.addHandler(ch)


class App(tk.Tk):
    def __init__(self):
        logger.debug("Initializing Tk app...")

        super().__init__()

        self.title("wgetTk")
        self.geometry("300x600")

        # URL label
        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.pack()

        # URL entry
        self.url = tk.StringVar()
        self.url_entry = ttk.Entry(self, textvariable=self.url)
        self.url_entry.focus()
        self.url_entry.pack()

        # Button
        self.button = ttk.Button(self, text="Click Me")
        self.button["command"] = self.button_clicked
        self.button.pack()

    def button_clicked(self):
        logger.debug("URL: %s", self.url.get())
        # wget -c -P ~/Downloads/ "https://domain.com/item"
        subprocess.run(
            ["wget", "-c", "-P", os.path.expanduser("~/Downloads/"), self.url.get()]
        )
        showinfo(title="Information", message="Download successful!")
