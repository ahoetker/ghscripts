#!/Users/andrew/anaconda/envs/matlab35/bin/python
# publish-mfile.py

import click
import os
import subprocess
import matlab.engine


@click.command()
@click.argument('mfile', type=click.Path(exists=True, resolve_path=True))
@click.argument('format')
@click.option('-t', is_flag=True, help="Use pdflatex to typeset output.")
@click.option('-v', is_flag=True, help="Verbose pdflatex messages.")


def publishMfile(mfile, format, t, v):
    """
    Use the MATLAB Engine to publish an mfile without needing to load the GUI.
    """
    if format not in ["html", "pdf", "latex", "xml"]:
        raise AttributeError("{} is not a valid format.".format(format))

    wd = os.path.split(mfile)[0]

    eng = matlab.engine.start_matlab()
    eng.cd(wd)
    eng.publish(mfile, format)
    eng.quit()

    if format == "latex" and t is True:
        filename = os.path.splitext(os.path.split(mfile)[1])[0] + ".tex"
        texfile = os.path.join(wd, "html", filename)
        typeset(texfile, v)

def typeset(texfile, v):
    os.chdir('html')
    if v is True:
        subprocess.call(['pdflatex', texfile], shell=False)
    else:
        devnull = open(os.devnull, 'w')
        subprocess.call(['pdflatex', texfile], shell=False, stdout=devnull)
        print("Typesetting complete (pdflatex).")

if __name__ == '__main__':
    publishMfile()
