#!/usr/bin/env python3.6

import click
import pyperclip

@click.command()
@click.option('-c', is_flag=True, help="Copy result to system clipboard.")
@click.argument('mfile', type=click.File('r'))


def printComment(c, mfile):
    """
    This script takes a MATLAB function .mfile and prints the function
    in MATLAB codeblock format. The comment can also be sent directly
    to the system clipboard. 
    """
    comment = "%%\n%\n"
    for line in mfile:
        comment += ( "%   " + str(line))

    if c is True:
        try:
            pyperclip.copy(comment)
            print("Comment copied to system clipboard.")
        except Exception as err:
            print(f"Exception raised: {err}")
            print("If you're on Linux, this is not surprising.")
            print("Try installing a recent version of PyQT.")
            print("Or run again without flag -c")
    else:
        print(comment)


if __name__ == '__main__':
    printComment()
