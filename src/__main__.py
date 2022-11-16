from os import path, remove, makedirs
from logic.layout import Layout
from logic.console import Console
import argparse
import sys

console = Console()

parser = argparse.ArgumentParser(
    description="Creates a basic python project structure.\n Space char '%20'")
parser.add_argument('-pn', '--projectname', required=True,
                    metavar='', help="The name of the project", type=str)
parser.add_argument('-d', '--dir', required=True, metavar='',
                    help="The directory to build the project structure in", type=str)
parser.add_argument('--mainfilename', default="__main__", metavar='',
                    help="The name of the main python file")
parser.add_argument('-u', '--ui', action="store_true",
                    help="Open the program in ui mode")
parser.add_argument('--vsc', action="store_true",
                    help="Open the project folder in vscode after creation")
# TODO: should I add a verbose function?


def main():
    workDir = path.dirname(path.abspath(__file__))
    args = parser.parse_args()

    console.print("Arguments:", str(args)[9:])
    console.print(f"UI Mode selected: {args.ui}")
    console.print(f"Opening vscode: {args.vsc}")

    if args.ui:
        pass
        # TODO: Run(args)
    else:  # Commandline running
        Layout(workDir, args.projectname, args.mainfilename, args.dir, args.vsc)
    #


if __name__ == "__main__":
    main()
