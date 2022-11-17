from typing import Self


class BaseBuilder():
    """Creates a customtkinter widget with a different initial process
    Args:
        ctkObject: customtkinter widget
        initProps: {init kwargs}
        placeProps: {place_cfg}
        children: dict[BaseBuilder]
    Funcs:
        make: (parent: Optional) -> CTkWidget: for internal and external use to build the gui object
    """

    def __init__(self, ctkObject: any = None, initProps: dict = None, placeProps: dict = None, children: list[Self] = None) -> any:
        if (not ctkObject) or (not initProps) or (not placeProps):
            raise TypeError(
                "ctkObject, initProps, placeProps must not be None")

        self.ctkObject = ctkObject
        self.initProps = initProps
        self.placeProps = placeProps
        self.children = children

        self.afterFunction = None

    def _createWidget(self, ctkObject, parent, initProps, placeProps, children):
        if parent:
            initProps["master"] = parent

        newWidget = ctkObject(**initProps)
        if placeProps:
            newWidget.place_configure(**placeProps)

        if children:
            self._addChildren(newWidget, children)

        return newWidget

    def _addChildren(self, parent, children):
        for _, v in enumerate(children):
            v.make(parent)

    def after(self, func: any) -> Self:
        """Sets a function to call after widget creation
        Args:
            func (w): Takes 1 argument of the widget
        """
        self.afterFunction = func
        return self

    def make(self, parent=None):
        """Makes the widget with the data at creation
        Args:
            parent (CTk object | None): The parent of the widget. Defaults to None.
        """
        widget = self._createWidget(
            self.ctkObject, parent, self.initProps, self.placeProps, self.children)

        if self.afterFunction:
            self.afterFunction(widget)

        return widget

# New(ctk.CTkButton, [{
#     "master": ctk.CTk(),
#     "text": "Hello!"
# }, {
#     "relwidth": 0.5,
#     "relheight": 0.5
# }], [
#     New(ctk.CTkButton, [{"text": "Smaller!"}, {
#         "relx": 0.25, "rely": 0.25, "relwidth": 0.5, "relheight": 0.5
#     }], [])
# ]).make()
# b = ctk.CTkButton(master=ctk.CTk(), text="Hello!")
# b.place_configure(relwidth=0.5, relheight=0.5)

# b = ctk.CTkButton(master=ctk.CTk(), text="Smaller!")
# b.place_configure(relx=0.25, rely=0.25, relwidth=0.5, relheight=0.5)
