"""
This scripts generates a slideshow from a specified notebook.

Usage:
python slides.py Lecture_X

Lecture_X is the name of the notebook to be converted.
"""

import os
import sys
from subprocess import call

if len(sys.argv) > 1:
    lecture = sys.argv[1]
else:
    raise RuntimeError("Lecture name not provided!")

call([
    "jupyter", "nbconvert",
    os.getcwd() + "\\{}.ipynb".format(lecture),
    "--to", "slides",
    "--post", "serve"])
