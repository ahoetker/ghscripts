#!/Users/andrew/anaconda/envs/matlab35/bin/python
# publishmfile.py

import click
import os
import subprocess
import matlab.engine


@click.command()
@click.argument('mfile', type=click.Path(exists=True, resolve_path=True))
@click.argument('format')
@click.option('-t', is_flag=True, help="Use pdflatex to typeset output.")
@click.option('-v', is_flag=True, help="Verbose pdflatex messages.")

def main(mfile, format, t, v):
    """
    Use the MATLAB Engine to publish an mfile without needing to load the GUI.
    """
    publishMfile(mfile, format, t, v)


def publishMfile(mfile, format, t, v):

    if format not in ["html", "pdf", "latex", "xml"]:
        raise AttributeError("{} is not a valid format.".format(format))

    wd, mfilename = os.path.split(mfile)

    eng = startEngine()
    eng.cd(wd)
    print("Publishing {} with format {}...".format(mfilename, format))
    eng.publish(mfile, format)
    eng.quit()
    print("Publishing complete")

    if format == "latex" and t is True:
        filename = os.path.splitext(os.path.split(mfile)[1])[0] + ".tex"
        texfile = os.path.join(wd, "html", filename)
        typeset(texfile, v)


def startEngine():
    if len(matlab.engine.find_matlab()) > 0:
        print("Connecting to shared MATLAB engine...")
        eng = matlab.engine.connect_matlab()
        print("Connected to {}".format(eng.matlab.engine.engineName()))
    else:
        print("No MATLAB engine found, starting new engine...")
        eng = matlab.engine.start_matlab()
        print("MATLAB engine started")

    return eng


def typeset(texfile, v):
    os.chdir('html')
    if v is True:
        subprocess.call(['pdflatex', texfile], shell=False)
    else:
        devnull = open(os.devnull, 'w')
        subprocess.call(['pdflatex', texfile], shell=False, stdout=devnull)

    print("Typesetting complete (pdflatex)")


if __name__ == '__main__':
    main()
