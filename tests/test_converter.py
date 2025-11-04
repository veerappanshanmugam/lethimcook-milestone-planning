"""Tests for core conversion functionality."""

import pytest
from lethimcook import convert


class TestVolumeConversions:
    """Test volume unit conversions."""

    def test_cups_to_ml(self):
        result = convert(2, "cups", "ml")
        assert abs(result - 473.176) < 0.01

    def test_tsp_to_tbsp(self):
        result = convert(3, "tsp", "tbsp")
        assert abs(result - 1) < 0.01

    def test_gallon_to_liter(self):
        result = convert(1, "gallon", "l")
        assert abs(result - 3.785) < 0.01

    def test_floz_to_ml(self):
        result = convert(8, "fl oz", "ml")
        assert abs(result - 236.588) < 0.01

    def test_same_unit(self):
        result = convert(5, "cup", "cup")
        assert result == 5


class TestWeightConversions:
    """Test weight unit conversions."""

    def test_pounds_to_grams(self):
        result = convert(1, "pound", "g")
        assert abs(result - 453.592) < 0.01

    def test_oz_to_grams(self):
        result = convert(16, "oz", "g")
        assert abs(result - 453.592) < 0.01

    def test_kg_to_lbs(self):
        result = convert(1, "kg", "lb")
        assert abs(result - 2.205) < 0.01

    def test_grams_to_ounces(self):
        result = convert(100, "g", "oz")
        assert abs(result - 3.527) < 0.01


class TestTemperatureConversions:
    """Test temperature unit conversions."""

    def test_fahrenheit_to_celsius(self):
        result = convert(32, "fahrenheit", "celsius")
        assert abs(result - 0) < 0.01

        result = convert(212, "f", "c")
        assert abs(result - 100) < 0.01

        result = convert(350, "f", "c")
        assert abs(result - 176.67) < 0.1

    def test_celsius_to_fahrenheit(self):
        result = convert(0, "celsius", "fahrenheit")
        assert abs(result - 32) < 0.01

        result = convert(100, "c", "f")
        assert abs(result - 212) < 0.01

    def test_celsius_to_kelvin(self):
        result = convert(0, "celsius", "kelvin")
        assert abs(result - 273.15) < 0.01

    def test_kelvin_to_celsius(self):
        result = convert(273.15, "kelvin", "celsius")
        assert abs(result - 0) < 0.01


class TestCountConversions:
    """Test count/item conversions."""

    def test_count_to_count(self):
        result = convert(5, "count", "item")
        assert result == 5


class TestErrorHandling:
    """Test error handling."""

    def test_incompatible_units(self):
        with pytest.raises(ValueError, match="Cannot convert between"):
            convert(1, "cups", "grams")

    def test_unknown_unit(self):
        with pytest.raises(ValueError, match="Unknown unit"):
            convert(1, "blorg", "ml")

    def test_temperature_weight_mix(self):
        with pytest.raises(ValueError, match="Cannot convert between"):
            convert(100, "celsius", "grams")


class TestUnitVariations:
    """Test different unit name variations."""

    def test_teaspoon_variations(self):
        result1 = convert(1, "tsp", "ml")
        result2 = convert(1, "teaspoon", "ml")
        assert abs(result1 - result2) < 0.001

    def test_pound_variations(self):
        result1 = convert(1, "lb", "g")
        result2 = convert(1, "lbs", "g")
        result3 = convert(1, "pound", "g")
        assert abs(result1 - result2) < 0.001
        assert abs(result1 - result3) < 0.001

    def test_case_insensitive(self):
        result1 = convert(1, "CUP", "ML")
        result2 = convert(1, "cup", "ml")
        assert abs(result1 - result2) < 0.001
