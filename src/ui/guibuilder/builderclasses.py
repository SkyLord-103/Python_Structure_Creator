import customtkinter as ctk
from .basebuilder import BaseBuilder


class XFrame(BaseBuilder):
    def __init__(self, init: dict = None, place: dict = None, children: list = None) -> any:
        super().__init__(ctk.CTkFrame, init, place, children)


class XButton(BaseBuilder):
    def __init__(self, init: dict = None, place: dict = None, children: list = None) -> any:
        super().__init__(ctk.CTkButton, init, place, children)


class XLabel(BaseBuilder):
    def __init__(self, init: dict = None, place: dict = None, children: list = None) -> any:
        super().__init__(ctk.CTkLabel, init, place, children)


class XEntry(BaseBuilder):
    def __init__(self, init: dict = None, place: dict = None, children: list = None) -> any:
        super().__init__(ctk.CTkEntry, init, place, children)


class XCheckBox(BaseBuilder):
    def __init__(self, init: dict = None, place: dict = None, children: list = None) -> any:
        super().__init__(ctk.CTkCheckBox, init, place, children)
