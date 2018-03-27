#!/usr/bin/env python3.6
# makereport.py - build MATLAB report from .m files and yaml

import yaml
import click
from publish-mfile.py import *

class Outline(yaml.YAMLObject):
    yaml_tag = u'!Outline'
    def __init__(self, header, problems, functions):
        self.header = header
        self.problems = problems
        self.functions = functions

@click.command()
@click.argument('yaml_file', type=click.File('r'))
@click.argument('output_file', type=click.File('w'))
@click.option('--funcs', is_flag=True, help="Append user functions.")

def makeReport(yaml_file, output_file, funcs):
    """
    Build a full m-file report for publication from indivudial mfiles.
    Structure is derived from YAML file.
    """
    outline = yaml.load(yaml_file)

    header = ""
    for txtfile in outline.header:
        with open(txtfile, 'r') as f:
            for line in f:
                header += line
        header += "\n\n"

    problems = ""
    for mfile in outline.problems:
        with open(mfile, 'r') as f:
            for line in f:
                problems += line
        problems += "\n\n"

    functions = ""
    if funcs is True:
        functions += "%% Referenced Functions \n"
        for func in outline.functions:
            with open(func, 'r') as f:
                comment = "%%\n%\n"
                for line in f:
                    comment += ( "%   " + str(line))
            functions += comment + "\n\n"

    report = header + problems + functions
    output_file.write(report)


if __name__ == '__main__':
    makeReport()
