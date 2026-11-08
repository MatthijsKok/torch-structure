"""
TorchStructure is a python package for graph-based autodifferentiable structural design
and engineering.
"""

from importlib.metadata import PackageNotFoundError, version

from . import (
    analysis,
    data,
    formfinding,
    generators,
    loader,
    loss,
    message_passing,
    plot,
    transforms,
    utils,
)

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = "0.0.0"

__all__ = [
    "analysis",
    "data",
    "formfinding",
    "generators",
    "loader",
    "message_passing",
    "loss",
    "plot",
    "transforms",
    "utils",
]
