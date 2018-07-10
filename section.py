#!/usr/bin/env python3

import click


@click.command()
@click.argument("words", nargs=-1)
def makesection(words):
    text = " ".join(words)
    middle = "# {} #".format(text)
    border = "#" * len(middle)
    section = "\n".join([border, middle, border])
    print(section)


if __name__ == "__main__":
    makesection()
