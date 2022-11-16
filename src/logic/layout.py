from os import path, mkdir, makedirs
from logic.console import Console
from subprocess import run
import json


def Log(*msg: str, end="\n"):
    print(f'layout.py - DEBUG: ', *msg, end=end)


console = Console()


def jsonReparse(pn: str, mfn: str, jsonData: dict) -> dict:
    rewrite = {}

    for key, value in jsonData.items():
        rewrite[key.replace("*;projectname*;",
                            pn).replace("*;mainfilename*;", mfn)] = value
    return rewrite


def Layout(workDir: str, projectName: str, mainFileName: str, installationDir: str, vsc: bool):
    if not installationDir or not workDir:
        raise TypeError("Expected 2 arguments!")

    def replaceKey(stri: str) -> str:
        return stri.replace("*;projectname*;", projectName).replace("*;mainfilename*;", mainFileName)

    installationDir = path.join(installationDir, projectName)
    console.print(
        f"Creating project folder: '{projectName}', at: '{installationDir}'")
    makedirs(installationDir, exist_ok=True)

    hierarchyJson = json.load(
        open(path.join(workDir, "data", "paths.json"), "r"))

    for _, rp in enumerate(hierarchyJson["folders"]):
        rk = replaceKey(rp)
        subDir = path.join(installationDir, rk)
        if not path.exists(subDir):
            console.print(f'Creating folder: [#30c5c4]{rk}')
            try:
                mkdir(subDir)
            except Exception as e:
                console.log(e)
                error = f' [red]{e}[/]' if e else ''
                console.print(
                    f'Couldn\'t create folder: [#30c5c4]{rk}[/]'+error)
        else:
            console.print(f'Folder already exists: [#30c5c4]{rk}')
    console.print('Finished creating folders')

    fileContents = jsonReparse(projectName, mainFileName, json.load(
        open(path.join(workDir, "data", "default_file_contents.json"), "r")))

    console.print("Creating files")
    for _, rp in enumerate(hierarchyJson["files"]):
        rk = replaceKey(rp)
        filePath = path.join(installationDir, *rk.split('\\'))

        if not path.exists(filePath):
            console.print(f'Creating file: [#30c5c4]{rk}')

            content = fileContents[rk]
            with open(filePath, "a") as f:
                sizeOfContent = len(content)

                for cIndex, s in enumerate(content):
                    endLine = "\n" if cIndex+1 != sizeOfContent else ''
                    f.write(replaceKey(s)+endLine)
        else:
            console.print(f'File already exists: [#30c5c4]{rk}')

    console.print('Finished creating files')

    if vsc:
        console.print("Opening [#1EA3FF]vscode")
        try:
            cmd = f"code {installationDir}"
            run(cmd, shell=True)
        except Exception as e:
            console.print_exception()
