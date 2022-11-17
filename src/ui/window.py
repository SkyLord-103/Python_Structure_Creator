from .guibuilder import XButton, XFrame, XEntry, XLabel, XCheckBox
from logic.layout import Layout
from logic.console import Console
from tkinter import filedialog
import customtkinter as ctk
from os import path


console = Console()


class Window(ctk.CTk):
    def __init__(self, workDir: str, cmdArgs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.workDir = workDir
        self.args = cmdArgs
        self.geometry("450x300")
        self.minsize(450, 300)

        self._createWidgets()

    def build(self) -> None:
        if not self.parseEntries():  # If the parse failed return
            console.print("[red]Parse failed.")
            return
        console.print("Arguments:", str(self.args)[9:], self.args.mainfilename)
        Layout(self.workDir, self.args.projectname, self.args.mainfilename, self.args.dir,
               self.args.copyrightyear, self.args.crfullname, self.args.vsc)

    def parseEntries(self) -> bool:
        if self.pnEntry.get():
            self.args.projectname = self.pnEntry.get()

        if self.mfnEntry.get():
            self.args.mainfilename = self.mfnEntry.get()

        if self.dirEntry.get():
            self.args.dir = self.dirEntry.get()

        if self.cYearEntry.get():
            self.args.copyrightyear = self.cYearEntry.get()
        if self.cfnEntry.get():
            self.args.crfullname = self.cfnEntry.get()
        self.args.vsc = bool(self.vscVar.get())

        if not path.exists(self.args.dir):
            console.print("[red]Build directory does not exist!")
            return 0
        if path.isfile(self.args.dir):
            console.print(
                "[red]Build path is not a directory!", self.args.dir)
            return 0

        return 1

    def repickDir(self):
        f = path.join(filedialog.askdirectory(
            mustexist=True, title="Select a folder"))
        if f:
            self.dirEntry.configure(placeholder_text=f)
            self.args.dir = f

    def _createWidgets(self):
        self.projectNameFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.05, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Project name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.pnEntry = XEntry({"master": self.projectNameFrame, "placeholder_text": self.args.projectname}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.mainfileFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.28, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Main file name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.mfnEntry = XEntry({"master": self.mainfileFrame, "placeholder_text": self.args.mainfilename}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.dirFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.51, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Build directory"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.dirEntry = XEntry({"master": self.dirFrame, "placeholder_text": self.args.dir}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.75, "relheight": 0.5}).make()

        self.dirButton = XButton({"master": self.dirFrame, "text": "Folder", "command": lambda: self.repickDir()}, {
            "relx": 0.8, "rely": 0.4, "relwidth": 0.175, "relheight": 0.5}).make()

        self.copyrightYearFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.05, "relwidth": 0.45, "relheight": 0.2}, [
                XLabel({"text": "Copyright year"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.cYearEntry = XEntry({"master": self.copyrightYearFrame, "placeholder_text": self.args.copyrightyear}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.crfullnameFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.28, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Copyright full name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.cfnEntry = XEntry({"master": self.crfullnameFrame, "placeholder_text": self.args.crfullname}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.vscCheckFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.51, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Open project in vscode"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        self.vscVar = ctk.IntVar()
        self.vscCheck = XCheckBox({"master": self.vscCheckFrame, "text": "Open vsc", "variable": self.vscVar}, {
            "relx": 0.25, "rely": 0.4, "relwidth": 0.5, "relheight": 0.5}).make()

        # Build Button
        XButton({"master": self, "text": "Build", "text_font": f'{ctk.ThemeManager.theme["text"]["font"]} 20', "command": lambda: self.build()}, {
            "relx": 0.03, "rely": 0.75, "relwidth": 0.94, "relheight": 0.2}).make()

        self.mainloop()


# ProjectName Entry                           | copyright year Entry

# mainfilename: __main__ Entry                | copyright full name Entry

# buildDir Entry, Button opens select dialog  | Open vsc Checkbox

#             ------------- Build -------------
