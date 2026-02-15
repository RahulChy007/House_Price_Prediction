"""
Configuration module for House Price Prediction project.
Contains all configuration settings, paths, and constants.
"""

import os
from pathlib import Path

# Project paths
PROJECT_ROOT = Path(__file__).parent.parent
DATA_DIR = PROJECT_ROOT / "data"
RAW_DATA_DIR = DATA_DIR / "raw"
PROCESSED_DATA_DIR = DATA_DIR / "processed"
MODELS_DIR = PROJECT_ROOT / "models"
NOTEBOOKS_DIR = PROJECT_ROOT / "notebooks"

# Ensure directories exist
for directory in [RAW_DATA_DIR, PROCESSED_DATA_DIR, MODELS_DIR]:
    directory.mkdir(parents=True, exist_ok=True)

# Data configuration
DATA_FILE = RAW_DATA_DIR / "housing.csv"
MODEL_FILE = MODELS_DIR / "model.pkl"

# Model parameters
TEST_SIZE = 0.2
RANDOM_STATE = 42
MODEL_TYPE = "LinearRegression"  # Can be changed to other models

# Feature configuration
FEATURES = ["area", "bedrooms", "bathrooms"]
TARGET = "price"

# Logging configuration
LOG_LEVEL = "INFO"
LOG_FORMAT = "%(__asctime__)s - %(name)s - %(levelname)s - %(message)s"

# Display configuration
CURRENCY_SYMBOL = "₹"
DECIMAL_PLACES = 2