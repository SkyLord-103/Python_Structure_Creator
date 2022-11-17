from tkinter import filedialog
import customtkinter as ctk
from .guibuilder import XButton, XFrame, XEntry, XLabel, XCheckBox
from logic.layout import Layout


class Window(ctk.CTk):
    def __init__(self, cmdArgs, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.args = cmdArgs
        self.geometry("450x300")

    def _createWidgets(self):
        self.projectNameFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.05, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Project name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        pnEntry = XEntry({"master": self.projectNameFrame, "placeholder_text": self.args.projectname}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.mainfileFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.28, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Main file name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        mfnEntry = XEntry({"master": self.mainfileFrame, "placeholder_text": self.args.mainfilename}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.dirFrame = XFrame({"master": self}, {
            "relx": 0.03, "rely": 0.51, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Build directory"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        dirEntry = XEntry({"master": self.dirFrame, "placeholder_text": self.args.dir}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.75, "relheight": 0.5}).make()

        def repickDir():
            self.args.dir = "C:\\Users\\r8gob"
            r = filedialog.askdirectory(
                title="Select a folder", mustexist=True)
            print(r, dirEntry.get())
            dirEntry.configure(placeholder_text=self.args.dir)

        dirButton = XButton({"master": self.dirFrame, "text": "Folder", "command": repickDir}, {
            "relx": 0.8, "rely": 0.4, "relwidth": 0.175, "relheight": 0.5}).make()

        self.copyrightYearFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.05, "relwidth": 0.45, "relheight": 0.2}, [
                XLabel({"text": "Copyright year"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        cYearEntry = XEntry({"master": self.copyrightYearFrame, "placeholder_text": self.args.copyrightyear}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.crfullnameFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.28, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Copyright full name"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        cfnEntry = XEntry({"master": self.crfullnameFrame, "placeholder_text": self.args.crfullname}, {
            "relx": 0.025, "rely": 0.4, "relwidth": 0.95, "relheight": 0.5}).make()

        self.vscCheckFrame = XFrame({"master": self}, {
            "anchor": ctk.NE, "relx": 0.97, "rely": 0.51, "relwidth": 0.45, "relheight": 0.2}, [
            XLabel({"text": "Open project in vscode"}, {"relx": 0.05, "rely": 0.05, "relwidth": 0.9, "relheight": 0.25})]).make()

        vscVar = ctk.IntVar()
        vscCheck = XCheckBox({"master": self.vscCheckFrame, "text": "Open vsc", "variable": vscVar}, {
            "relx": 0.25, "rely": 0.4, "relwidth": 0.5, "relheight": 0.5}).make()

        buildButton = XButton({"master": self, "text": "Build", "text_font": f'{ctk.ThemeManager.theme["text"]["font"]} 20', "command": lambda: print("Building")}, {
            "relx": 0.03, "rely": 0.75, "relwidth": 0.94, "relheight": 0.2}).make()

        self.mainloop()


# ProjectName Entry                           | copyright year Entry

# mainfilename: __main__ Entry                | copyright full name Entry

# buildDir Entry, Button opens select dialog  | Open vsc Checkbox

#             ------------- Build -------------
