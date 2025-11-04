"""Natural language conversion utility using regex and string matching."""

import re
from lethimcook.converter import convert


def _format_number(value: float) -> str:
    """Format a number, removing .0 for integers."""
    if value == int(value):
        return str(int(value))
    return str(value)


def convert_natural(text: str) -> str:
    """
    Convert using natural language input.

    Supports patterns like:
    - "2 cups to ml"
    - "convert 1.5 pounds to grams"
    - "how many ml in 3 teaspoons"
    - "5 fahrenheit to celsius"

    Args:
        text: Natural language conversion request

    Returns:
        Formatted string with conversion result

    Raises:
        ValueError: If the input cannot be parsed
    """
    text = text.lower().strip()

    # Pattern 1: "X unit to unit" or "X unit in unit"
    pattern1 = r"(\d+\.?\d*)\s+([a-z\s]+?)\s+(?:to|in)\s+([a-z\s]+)"
    match = re.match(pattern1, text)
    if match:
        value = float(match.group(1))
        from_unit = match.group(2).strip()
        to_unit = match.group(3).strip()
        result = convert(value, from_unit, to_unit)
        return f"{_format_number(value)} {from_unit} = {result:.2f} {to_unit}"

    # Pattern 2: "convert X unit to unit"
    pattern2 = r"convert\s+(\d+\.?\d*)\s+([a-z\s]+?)\s+to\s+([a-z\s]+)"
    match = re.match(pattern2, text)
    if match:
        value = float(match.group(1))
        from_unit = match.group(2).strip()
        to_unit = match.group(3).strip()
        result = convert(value, from_unit, to_unit)
        return f"{_format_number(value)} {from_unit} = {result:.2f} {to_unit}"

    # Pattern 3: "how many unit in X unit"
    pattern3 = r"how\s+many\s+([a-z\s]+?)\s+in\s+(\d+\.?\d*)\s+([a-z\s]+)"
    match = re.match(pattern3, text)
    if match:
        to_unit = match.group(1).strip()
        value = float(match.group(2))
        from_unit = match.group(3).strip()
        result = convert(value, from_unit, to_unit)
        return f"{_format_number(value)} {from_unit} = {result:.2f} {to_unit}"

    raise ValueError(
        f"Could not parse conversion request: {text}\n"
        "Try formats like: '2 cups to ml' or 'convert 1 pound to grams'"
    )
