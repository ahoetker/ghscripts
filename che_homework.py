#!/usr/bin/env python3
from pathlib import Path
import sys

unitstring_code = r"""function displayString = unitString(quantity, name)
%UNITSTRING Display a 1x2 sym with symbolic units
% USAGE: unitString(some_quantity, name)
% OUTPUT:
%   - displayString: char vector containing name, scalar, and units
if nargin < 2
    n = inputname(1);
else
    n = name;
end

[s, U] = separateUnits(quantity);
formatSpec = '%s: %s %s';
displayString = sprintf(formatSpec, n, num2str(double(s)), symunit2str(U));
end"""

preamble_code = r"""% Math stuff
\usepackage{amsmath}
\usepackage{amsfonts}
\usepackage{amssymb}
% Fancy references
\usepackage{varioref}
\labelformat{equation}{equation~(#1)}
% XeLaTeX Fonts
\usepackage{unicode-math}
\setmainfont{STIX2Text-Regular.otf}
\setmathfont{STIX2Math.otf}
% Hyperlinks
\usepackage{color}
\definecolor{mygrey}{gray}{0.25}
\usepackage[pdfborder=0, colorlinks=true, urlcolor=blue, linkcolor=mygrey]{hyperref}
% Page layout
\usepackage[margin=1in]{geometry}
% Header definition
\usepackage{fancyhdr}
\pagestyle{fancy}
\lhead{Andrew Hoetker - ASUID 1207233777}
\rhead{CHE 334 Homework 12}"""

def create_header(assn_name = "ASSN NAME", due_date="DUE DATE", class_text="CLASS TEXT"):
    header_text = r"""%% ASSN NAME"""
    return header_text


def create_homework():
    homework_name = str(sys.argv[1])
    homework_dir = Path(homework_name)
    Path.mkdir(homework_dir)
    header_file = Path(homework_dir / "header.m")
    unitstring_file = Path(homework_dir / "unitString.m")
    preamble_file = Path(homework_dir / "preamble.tex")
    with header_file.open("w") as f:
        f.write(create_header(assn_name=homework_name))
    with unitstring_file.open("w") as f:
        f.write(unitstring_code)
    with preamble_file.open("w") as f:
        f.write(preamble_code)


if __name__ == "__main__":
    create_homework()
