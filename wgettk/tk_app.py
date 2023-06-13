import logging
import sys
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo, showerror
from . import wget_wrapper
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
        self.geometry("510x50")
        self.create_grid()
        self.create_widgets()

    def create_grid(self) -> None:
        logger.debug("Creating grid....")
        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)
        self.columnconfigure(2, weight=2)
        self.columnconfigure(3, weight=2)

    def create_widgets(self) -> None:
        logger.debug("Loading widgets....")

        # URL label
        self.url_label = ttk.Label(self, text="URL:")
        self.url_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        # URL entry
        self.url = tk.StringVar()
        self.url_entry = ttk.Entry(self, textvariable=self.url)
        self.url_entry.focus()
        self.url_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        # Button
        self.button = ttk.Button(self, text="Download")
        self.button["command"] = self.button_clicked
        self.button.grid(column=2, row=0, sticky=tk.E, padx=5, pady=5)

        # Dropdown
        self.dropdown_choice = tk.StringVar()
        dropdown_arr = [
            "Single File",
            "Folder",
            "Folder - Recursive",
            "All Images",
            "All Images - Recursive",
        ]
        self.dropdown = ttk.OptionMenu(
            self, self.dropdown_choice, dropdown_arr[0], *dropdown_arr
        )
        self.dropdown.grid(column=3, row=0, sticky=tk.W)

    def button_clicked(self) -> None:
        logger.debug("Button pressed, downloading: %s....", self.url.get())
        download_successful = wget_wrapper.basic_download(
            self.url.get(), os.path.expanduser("~/Downloads/")
        )
        if download_successful:
            showinfo(title="Information", message="Download successful!")
        else:
            showerror(
                title="Error",
                message="Unable to download file. Check the url and try again",
            )
