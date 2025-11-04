"""Unit conversion definitions and constants."""

from enum import StrEnum


class UnitType(StrEnum):
    VOLUME = "volume"
    WEIGHT = "weight"
    TEMPERATURE = "temperature"
    COUNT = "count"


# Base units for each type
BASE_UNITS = {
    UnitType.VOLUME: "ml",
    UnitType.WEIGHT: "g",
    UnitType.TEMPERATURE: "celsius",
    UnitType.COUNT: "count",
}

# Conversion factors to base units
# For volume and weight: multiply by this to get base unit
CONVERSIONS = {
    # Volume (to milliliters)
    "tsp": 4.92892,
    "teaspoon": 4.92892,
    "teaspoons": 4.92892,
    "tbsp": 14.7868,
    "tablespoon": 14.7868,
    "tablespoons": 14.7868,
    "floz": 29.5735,
    "fl oz": 29.5735,
    "fluid ounce": 29.5735,
    "fluid ounces": 29.5735,
    "cup": 236.588,
    "cups": 236.588,
    "pint": 473.176,
    "pints": 473.176,
    "quart": 946.353,
    "quarts": 946.353,
    "gallon": 3785.41,
    "gallons": 3785.41,
    "ml": 1.0,
    "milliliter": 1.0,
    "milliliters": 1.0,
    "l": 1000.0,
    "liter": 1000.0,
    "liters": 1000.0,

    # Weight (to grams)
    "oz": 28.3495,
    "ounce": 28.3495,
    "ounces": 28.3495,
    "lb": 453.592,
    "lbs": 453.592,
    "pound": 453.592,
    "pounds": 453.592,
    "g": 1.0,
    "gram": 1.0,
    "grams": 1.0,
    "kg": 1000.0,
    "kilogram": 1000.0,
    "kilograms": 1000.0,

    # Count (dimensionless)
    "count": 1.0,
    "item": 1.0,
    "items": 1.0,
    "piece": 1.0,
    "pieces": 1.0,
    "whole": 1.0,
}

# Unit type mapping
UNIT_TYPES = {
    # Volume
    "tsp": UnitType.VOLUME,
    "teaspoon": UnitType.VOLUME,
    "teaspoons": UnitType.VOLUME,
    "tbsp": UnitType.VOLUME,
    "tablespoon": UnitType.VOLUME,
    "tablespoons": UnitType.VOLUME,
    "floz": UnitType.VOLUME,
    "fl oz": UnitType.VOLUME,
    "fluid ounce": UnitType.VOLUME,
    "fluid ounces": UnitType.VOLUME,
    "cup": UnitType.VOLUME,
    "cups": UnitType.VOLUME,
    "pint": UnitType.VOLUME,
    "pints": UnitType.VOLUME,
    "quart": UnitType.VOLUME,
    "quarts": UnitType.VOLUME,
    "gallon": UnitType.VOLUME,
    "gallons": UnitType.VOLUME,
    "ml": UnitType.VOLUME,
    "milliliter": UnitType.VOLUME,
    "milliliters": UnitType.VOLUME,
    "l": UnitType.VOLUME,
    "liter": UnitType.VOLUME,
    "liters": UnitType.VOLUME,

    # Weight
    "oz": UnitType.WEIGHT,
    "ounce": UnitType.WEIGHT,
    "ounces": UnitType.WEIGHT,
    "lb": UnitType.WEIGHT,
    "lbs": UnitType.WEIGHT,
    "pound": UnitType.WEIGHT,
    "pounds": UnitType.WEIGHT,
    "g": UnitType.WEIGHT,
    "gram": UnitType.WEIGHT,
    "grams": UnitType.WEIGHT,
    "kg": UnitType.WEIGHT,
    "kilogram": UnitType.WEIGHT,
    "kilograms": UnitType.WEIGHT,

    # Temperature
    "fahrenheit": UnitType.TEMPERATURE,
    "f": UnitType.TEMPERATURE,
    "celsius": UnitType.TEMPERATURE,
    "c": UnitType.TEMPERATURE,
    "kelvin": UnitType.TEMPERATURE,
    "k": UnitType.TEMPERATURE,

    # Count
    "count": UnitType.COUNT,
    "item": UnitType.COUNT,
    "items": UnitType.COUNT,
    "piece": UnitType.COUNT,
    "pieces": UnitType.COUNT,
    "whole": UnitType.COUNT,
}


def normalize_unit(unit: str) -> str:
    """Normalize unit string to lowercase and strip whitespace."""
    return unit.lower().strip()


def get_unit_type(unit: str) -> UnitType:
    """Get the type of a unit."""
    normalized = normalize_unit(unit)
    if normalized not in UNIT_TYPES:
        raise ValueError(f"Unknown unit: {unit}")
    return UNIT_TYPES[normalized]
