import torch

from .data import StructData
from .dataset import Dataset, LegacyDataset, save
from .utils import requires_metadata
from .view import NodeView

__all__ = ["Dataset", "LegacyDataset", "NodeView", "StructData", "requires_metadata", "save"]

torch.serialization.add_safe_globals([StructData])
