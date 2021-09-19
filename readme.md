# Baby Schedule

## Overview

This repo is to generate a plot from a csv of baby activity (e.g. naps, feeding, etc.)

Structure of csv is as follows:

file header: (i.e. Week #)
header: time,activity,notes
each day starts with a "-" then date
entries
etc.

## To Use:

1. install python 3 requirements `pip install -r requirements.txt` (or equivalent)
2. run `plotter.py` with chosen .csv (e.g. python3 plotter.py example.csv)
3. outputs images and summary.html to view plots

## Notes:
This is a minimal implementation to generate plots. Much could be improved.
