"""
Quantum Energy Forecasting Package

Quantum-Ready, Weather-Aware Kernel Forecasting for High-Resolution 
Electricity Demand & Market Insights
"""

__version__ = "0.1.0"
__author__ = "ol-s-cloud"
__email__ = "contact@ol-s-cloud.dev"

from .core.forecaster import QuantumEnergyForecaster
from .core.quantum_kernels import QuantumKernelSVM, QuantumFeatureMap
from .data.weather import WeatherDataCollector
from .data.energy import EnergyDataCollector
from .models.ensemble import EnsembleForecaster
from .utils.config import Config

__all__ = [
    "QuantumEnergyForecaster",
    "QuantumKernelSVM",
    "QuantumFeatureMap",
    "WeatherDataCollector",
    "EnergyDataCollector",
    "EnsembleForecaster",
    "Config",
]
