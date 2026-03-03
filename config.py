"""
Configuration for Mnemosyne's Bargain Cognitive Cache.
All memory-critical parameters are optimized for <50MB total footprint.
"""
import os
from dataclasses import dataclass
from typing import Dict, Any
from enum import Enum

class FeatureStrategy(Enum):
    """Memory-efficient feature extraction strategies."""
    MINIMAL_TA = 1  # Only 5 key technical indicators
    QUANTIZED_SENTIMENT = 2  # 8-bit quantized sentiment scores
    COMPRESSED_WINDOW = 3  # Compressed rolling windows

@dataclass
class CacheConfig:
    """Memory-constrained cache configuration."""
    MAX_CACHE_ENTRIES: int = 1000  # Strict limit
    CACHE_ENTRY_SIZE_BYTES: int = 512  # 512 bytes per entry
    QUANTIZATION_BITS: int = 8  # 8-bit quantization for features
    COMPRESSION_LEVEL: int = 9  # Maximum compression
    
    # Feature engineering constraints
    MAX_FEATURES: int = 7
    FEATURE_WINDOW_SIZE: int = 20  # Reduced from typical 50-100
    SENTIMENT_LOOKBACK: int = 5  # Only last 5 sentiment readings
    
    # Prediction constraints
    MODEL_MAX_SIZE_MB: float = 2.0
    PREDICTION_BATCH_SIZE: int = 10

@dataclass
class APIConfig:
    """SaaS API configuration."""
    API_VERSION: str = "v1.0"
    REQUEST_RATE_LIMIT: int = 100  # Requests per hour per key
    RESPONSE_CACHE_TTL: int = 300