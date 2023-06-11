import os
from .. import wget_wrapper


def test_basic_download_success(tmp_path):
    wget_wrapper.basic_download(
        "https://www.gutenberg.org/files/5200/5200-0.txt", tmp_path
    )
    file_path = os.path.join(tmp_path, "5200-0.txt")
    assert os.path.exists(file_path)
    first_line = ""

    with open(file_path, encoding="utf-8-sig") as file:
        first_line = file.readline().strip("\n")

    assert first_line == "The Project Gutenberg eBook of Metamorphosis, by Franz Kafka"


def test_basic_download_failure():
    download_successful = wget_wrapper.basic_download("", "")
    assert download_successful == False
