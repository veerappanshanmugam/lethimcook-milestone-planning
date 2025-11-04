# Measure

A Python library for converting between units of measurement, particularly focused on cooking and recipes.

## Features

- Convert between common cooking measurements (volume, weight, temperature)
- Natural language input for conversions (e.g., "2 cups to ml")
- Recipe scaling utility to adjust ingredient quantities for different serving sizes
- Simple, intuitive API

## Installation

```bash
pip install -e .
```

## Usage

### Basic unit conversion

```python
from measure import convert

# Convert between units
result = convert(2, "cups", "ml")
print(result)  # 473.176

result = convert(350, "fahrenheit", "celsius")
print(result)  # 176.67
```

### Natural language conversion

```python
from measure import convert_natural

# Use natural language for conversions
result = convert_natural("2 cups to ml")
print(result)  # "2 cups = 473.18 ml"

result = convert_natural("convert 1 pound to grams")
print(result)  # "1 pound = 453.59 grams"
```

### Recipe scaling

```python
from measure import scale_recipe

recipe = {
    "servings": 4,
    "ingredients": [
        {"amount": 2, "unit": "cups", "name": "flour"},
        {"amount": 1, "unit": "tsp", "name": "salt"},
        {"amount": 3, "unit": "eggs", "name": "eggs"},
    ]
}

scaled = scale_recipe(recipe, new_servings=8)
# Doubles all ingredient amounts
```

## Supported units

### Volume
- teaspoon (tsp), tablespoon (tbsp), fluid ounce (fl oz, floz)
- cup, pint, quart, gallon
- milliliter (ml), liter (l)

### Weight
- ounce (oz), pound (lb, lbs)
- gram (g), kilogram (kg)

### Temperature
- fahrenheit (f), celsius (c), kelvin (k)

## License

MIT
