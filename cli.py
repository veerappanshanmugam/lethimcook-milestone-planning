#!/usr/bin/env python3
"""Command-line interface for the lethimcook library."""

import sys

from lethimcook import convert_natural


def main():
    """Simple CLI for unit conversions."""
    if len(sys.argv) < 2:
        print("LetHimCook - Unit Conversion Library")
        print("\nUsage:")
        print("  python cli.py '2 cups to ml'")
        print("  python cli.py 'convert 1 pound to grams'")
        print("  python cli.py 'how many ml in 3 teaspoons'")
        print("\nSupported units:")
        print("  Volume: tsp, tbsp, fl oz, cup, pint, quart, gallon, ml, liter")
        print("  Weight: oz, pound, gram, kilogram")
        print("  Temperature: fahrenheit, celsius, kelvin")
        sys.exit(1)

    query = " ".join(sys.argv[1:])

    try:
        result = convert_natural(query)
        print(result)
    except ValueError as e:
        print(f"Error: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
