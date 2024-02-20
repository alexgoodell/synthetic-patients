
###################################################################################
# ALEX'S UTILITIES
#
# alternatively
# url = "https://alx.gd/util"
# with httpimport.remote_repo(url):
#   import util
#


import json
import os
import shlex
import struct
import platform
import subprocess
import tabulate
from IPython.display import clear_output
import rich
import datetime
import time
import random
import string
import pandas as pd
import logging
import importlib

import numpy as np
from pathlib import Path
import inspect
import sys


# # allow saving / uploading of chart to plotly
# import chart_studio.plotly as py
# import plotly.figure_factory as ff
# import chart_studio.plotly as pfig
#
#
# def upload_fig(fig, filename):
#     plotly_api_key = 'mPkErN0mUaVwGWg8ll2x'
#     plotly_username = 'alexgoodell'
#     from chart_studio.tools import set_credentials_file
#     # Plotly Chart Studio authentication
#     set_credentials_file(
#         username=plotly_username,
#         api_key=plotly_api_key
#     )
#     chart_url = py.plot(fig,filename=filename,auto_open=False,fileopt='overwrite',sharing='public')
#     print(f"View this figure on [Plotly]({chart_url})")
#     return chart_url

def find_root_from_readme():
    # Attempt to find README.md in the current directory and up two levels
    max_levels_up = 2
    current_dir = os.path.abspath(os.curdir)

    for _ in range(max_levels_up + 1):
        # Construct the path to where README.md might be
        readme_path = os.path.join(current_dir, "README.md")

        # Check if README.md exists at this path
        if os.path.isfile(readme_path):
            # Return the absolute path if found
            return os.path.dirname(os.path.abspath(readme_path))

        # Move up one directory level
        current_dir = os.path.dirname(current_dir)

    # Return None if README.md was not found
    return None


ROOT_DIR = find_root_from_readme()
PAPER_DIR = os.path.join(ROOT_DIR, 'manuscript')
FIG_DIR = os.path.join(PAPER_DIR, 'figures')

pd.set_option('display.max_colwidth', 70)


def configure_logging():
    logging.basicConfig(filename=f"{ROOT_DIR}/logs/log.txt",
                        filemode='w',
                        format='%(asctime)s,%(msecs)d %(name)s %(levelname)s %(message)s',
                        datefmt='%Y-%m-%d %H:%M',
                        level=logging.DEBUG)


def get_root_dir():
    # assumes in the root/utilities folder
    return os.path.dirname(os.path.abspath("../README.md"))


def get_fig_dir():
    return get_root_dir() + "/manuscript/figures"


def reload():
    importlib.reload(util)


def generate_random_string():
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(2)) + ''.join(
        random.choice(string.digits) for _ in range(2)) + ''.join(
        random.choice(string.ascii_lowercase) for _ in range(2)) + ''.join(
        random.choice(string.digits) for _ in range(2)) + ''.join(
        random.choice(string.ascii_lowercase) for _ in range(2))


def wait_rand():
    wait_time = random.randint(1, 3)
    time.sleep(wait_time)


def log_and_print(text):
    logging.info(text)
    print(text)


def log(text):
    logging.info(text)


def get_timestamp():
    timestamp = '{:%Y-%m-%d-T-%H-%M-%S}'.format(datetime.datetime.now())
    return timestamp


def printl(text):
    print(text, end="")


def cprint(text):
    clear_output(wait=True)
    print(text, flush=True)


def cr_print(text):
    clear_output(wait=True)
    rich.print(text, flush=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def tab_cols(df, cns):
    for cn in cns:
        print("\n\n{}".format(titlecase(cn)))
        print(tabulate.tabulate(pd.DataFrame(df[cn].value_counts()), tablefmt="pipe", headers=['Name', 'Count']))


def tab(df, tbformat="heavy_grid"):
    print(tabulate.tabulate(df, headers='keys', tablefmt=tbformat, showindex=False))


def header(m):
    length = get_terminal_size()[0]
    print(colored(m, 'yellow'))
    print(colored('▒' * length, 'white'))


def alert(m, error_code):
    text_color = ['green', 'yellow', 'red', 'white'][error_code]
    length = get_terminal_size()[0]
    print(colored('\n   > ' + m, text_color))


def hr():
    length = get_terminal_size()[0]
    print(colored('-' * length, 'white'))


if __name__ == "__main__":
    print("hello world")
