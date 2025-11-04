"""Core unit conversion functionality."""

from lethimcook.units import (
    CONVERSIONS,
    UnitType,
    get_unit_type,
    normalize_unit,
)


def convert(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a value from one unit to another.

    Args:
        value: The numeric value to convert
        from_unit: The source unit
        to_unit: The target unit

    Returns:
        The converted value

    Raises:
        ValueError: If units are incompatible or unknown
    """
    from_unit = normalize_unit(from_unit)
    to_unit = normalize_unit(to_unit)

    # Get unit types
    from_type = get_unit_type(from_unit)
    to_type = get_unit_type(to_unit)

    # Check compatibility
    if from_type != to_type:
        raise ValueError(
            f"Cannot convert between {from_type} and {to_type}"
        )

    # Handle temperature separately (non-linear conversion)
    if from_type == UnitType.TEMPERATURE:
        return _convert_temperature(value, from_unit, to_unit)

    # Handle count (no conversion needed)
    if from_type == UnitType.COUNT:
        return value

    # Convert: from_unit -> base_unit -> to_unit
    base_value = value * CONVERSIONS[from_unit]
    result = base_value / CONVERSIONS[to_unit]

    return result


def _convert_temperature(value: float, from_unit: str, to_unit: str) -> float:
    """Convert temperature between different scales."""
    # First convert to Celsius
    match from_unit:
        case "celsius" | "c":
            celsius = value
        case "fahrenheit" | "f":
            celsius = (value - 32) * 5 / 9
        case "kelvin" | "k":
            celsius = value - 273.15
        case _:
            raise ValueError(f"Unknown temperature unit: {from_unit}")

    # Then convert from Celsius to target
    match to_unit:
        case "celsius" | "c":
            return celsius
        case "fahrenheit" | "f":
            return celsius * 9 / 5 + 32
        case "kelvin" | "k":
            return celsius + 273.15
        case _:
            raise ValueError(f"Unknown temperature unit: {to_unit}")
