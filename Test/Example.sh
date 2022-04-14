#!/bin/sh


# Make this file work from any pwd
folder=$(dirname "$0")

alias plot="$folder/../Source/Plot.py"
csv="$folder/Work_Right.csv"

plot $csv line