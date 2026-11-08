from .fem import FEM, StiffnessAggregator
from .laplace import Laplacian
from .lignn import LocalLogicLoss, WeightedMax
from .residual_force import ResidualForce

__all__ = [
    "FEM",
    "Laplacian",
    "LocalLogicLoss",
    "ResidualForce",
    "StiffnessAggregator",
    "WeightedMax",
]
