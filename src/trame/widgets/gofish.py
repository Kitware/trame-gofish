from trame_gofish.widgets.gofish import *  # noqa: F403


def initialize(server):
    from trame_gofish import module

    server.enable_module(module)
