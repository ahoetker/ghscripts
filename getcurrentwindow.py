#!/usr/bin/env python3.6

import subprocess
from time import sleep

def filterWindowTitle():
    w = subprocess.check_output(["xdotool", "getwindowfocus", "getwindowname"])
    title = str(w)
    common_applications = [
        "Chromium",
        "Atom",
        "Terminal",
        "File Manager",
        "Desktop",
        "Spyder",
    ]
    for appname in common_applications:
        if title.find(appname) != -1:
            return appname

    title = title[2:-3]
    return title


def main():
    print(filterWindowTitle())

if __name__=='__main__':
    main()
