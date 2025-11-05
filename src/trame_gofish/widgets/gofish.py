from trame_client.widgets.core import AbstractElement

from .. import module


class HtmlElement(AbstractElement):
    def __init__(self, _elem_name, children=None, **kwargs):
        super().__init__(_elem_name, children, **kwargs)
        if self.server:
            self.server.enable_module(module)


__all__ = [
    "GoFishGraph",
]


class GoFishGraph(HtmlElement):
    def __init__(self, **kwargs):
        super().__init__(
            "GoFishGraph",
            **kwargs,
        )
        self._attr_names += [
            "data",
        ]
        self._event_names += [
            "update",
        ]
