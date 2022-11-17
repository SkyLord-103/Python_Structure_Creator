"""Parses text from input.txt into a json (almost) ready script, then exports to output.txt"""
from os import path

workDir = path.dirname(path.abspath(__file__))

inputFile = path.join(workDir, "input.txt")
outputFile = path.join(workDir, "output.txt")


if not path.exists(inputFile):
    raise FileNotFoundError(f"No such file {inputFile}")


with open(outputFile, "a") as output:
    with open(inputFile, "r") as reading:
        output.write("[\n")

        lines = reading.readlines()
        for index, line in enumerate(lines):
            cleaned = line.strip("\n").replace('"', '\\"').replace(
                r"\'", r"\\'")

            endComma = ',' if index+1 != len(lines) else ''
            preparedText = f'"{cleaned}"{endComma}'
            output.write(preparedText+"\n")
        output.write("]")
