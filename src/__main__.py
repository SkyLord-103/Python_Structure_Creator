from os import path, remove, makedirs
from logic.console import Console
from logic.layout import Layout
from ui.window import Window
import argparse

console = Console()

parser = argparse.ArgumentParser(
    description="Creates a basic python project structure.\n Space char '%20'")
parser.add_argument('-ui', '--uimode', action="store_true",
                    help="Open the program in ui mode")
parser.add_argument('-vsc', '--vsc', action="store_true",
                    help="Open the project folder in vscode after creation")

parser.add_argument('-pn', '--projectname', required=True,
                    metavar='', help="The name of the project", type=str)
parser.add_argument('-mfn', '--mainfilename', default="__main__", metavar='',
                    help="The name of the main python file")
parser.add_argument('-cy', '--copyrightyear', default="[year]", metavar='',
                    help="The year of the copy right in the license file")
parser.add_argument('-cfn', '--crfullname', default="[fullname]", metavar='',
                    help="The full name for the copyright in the license file")
parser.add_argument('-d', '--dir', required=True, metavar='',
                    help="The directory to build the project structure in", type=str)

# TODO: should I add a verbose function?


def main():
    workDir = path.dirname(path.abspath(__file__))
    args = parser.parse_args()

    console.print("Arguments:", str(args)[9:])
    console.print(f"UI Mode selected: {args.uimode}")
    console.print(f"Opening vscode: {args.vsc}")

    if args.uimode:
        Window(workDir, args)
    else:  # Commandline running
        Layout(workDir, args.projectname, args.mainfilename, args.dir,
               args.copyrightyear, args.crfullname, args.vsc)
    #


if __name__ == "__main__":
    main()
