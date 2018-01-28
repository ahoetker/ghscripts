#!/usr/bin/env python3.6
# archiver.py - copy directory to location and compress it
# created largely to learn about click and shutil

import click
from shutil import copytree, rmtree, make_archive
from time import strftime

@click.command()
@click.option('-v', is_flag=True, help="Enable verbose mode.")
@click.argument('src', type=click.Path(exists=True, resolve_path=True))
@click.argument('dest', type=click.Path(resolve_path=True))

def copyDir(v, src, dest):
    """
    This program copies the SRC directory to DEST. If the DEST directory
    already exists, it will be moved to a timestamped .zip archive.
    """
    if v is True:
        print(f"Copying {src} to {dest}")
    try:
        copytree(src, dest)
    except FileExistsError:
        compressDir(v, dest)
        rmtree(dest)
        copytree(src, dest)


def compressDir(v, dir_to_compress):
    timestr = strftime("%Y-%m-%d")
    archive_name = f"{dir_to_compress}-{timestr}"
    if v is True:
        print(f"Archiving {dir_to_compress} to {archive_name}.zip")
    make_archive(archive_name, 'zip', dir_to_compress)


if __name__ == '__main__':
    copyDir()
