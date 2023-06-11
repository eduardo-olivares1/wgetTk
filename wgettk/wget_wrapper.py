import subprocess
import logging
import sys

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


def basic_download(url: str, save_path: str) -> bool:
    """Basic single file download using wget

    Parameters
    ----------
    url : str
        URL of file or page
    save_path : str
        Location to save file to

    Returns
    -------
    bool
        Boolean success indicator. Returns True on success
    """
    try:
        # wget -c -P ~/Downloads/ "https://domain.com/item"
        subprocess.run(
            ["wget", "-c", "-P", save_path, url],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.STDOUT,
            check=True,
        )
        logger.debug("Downloaded %s to %s", url, save_path)
        return True
    except subprocess.CalledProcessError as error:
        logger.error("%s", error)
        return False
