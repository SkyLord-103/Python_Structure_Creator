import customtkinter as ctk
from .guibuilder import XButton, XFrame, XEntry, XLabel
from logic.layout import Layout


def Run(args):
    window = ctk.CTk()
    window.geometry("450x300")

    XEntry({"master": window, "placeholder_text": "File name: " + args.mainfilename, "text_font": f'{ctk.ThemeManager.theme["text"]["font"]} 20'}, {
        "relx": 0.025, "rely": 0.2, "relwidth": 0.95, "relheight": 0.2}).make()

    XButton({"master": window, "text": "Build", "text_font": f'{ctk.ThemeManager.theme["text"]["font"]} 20', "command": lambda: print("Building")}, {
            "relx": 0.025, "rely": 0.75, "relwidth": 0.95, "relheight": 0.2}).make()

    window.mainloop()


# ProjectName Entry                           | copyright year Entry

# mainfilename: __main__ Entry                | copyright full name Entry

# buildDir Entry, Button opens select dialog  | Open vsc Checkbox

#             ------------- Build -------------
