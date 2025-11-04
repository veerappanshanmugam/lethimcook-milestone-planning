"""Tests for natural language conversion."""

import pytest
from lethimcook import convert_natural


class TestNaturalLanguagePatterns:
    """Test various natural language input patterns."""

    def test_basic_to_pattern(self):
        result = convert_natural("2 cups to ml")
        assert "2 cups" in result.lower()
        assert "ml" in result.lower()
        assert "473" in result

    def test_convert_pattern(self):
        result = convert_natural("convert 1 pound to grams")
        assert "1 pound" in result.lower()
        assert "gram" in result.lower()
        assert "453" in result

    def test_how_many_pattern(self):
        result = convert_natural("how many ml in 3 teaspoons")
        assert "3 teaspoon" in result.lower()
        assert "ml" in result.lower()

    def test_decimal_values(self):
        result = convert_natural("1.5 cups to ml")
        assert "1.5" in result

    def test_temperature_conversion(self):
        result = convert_natural("350 fahrenheit to celsius")
        assert "350" in result
        assert "fahrenheit" in result.lower()
        assert "celsius" in result.lower()

    def test_case_insensitive(self):
        result1 = convert_natural("2 CUPS to ML")
        result2 = convert_natural("2 cups to ml")
        # Both should contain the same numeric result
        assert "473" in result1
        assert "473" in result2

    def test_multi_word_units(self):
        result = convert_natural("5 fluid ounce to ml")
        assert "fluid ounce" in result.lower()
        assert "ml" in result.lower()


class TestNaturalLanguageErrors:
    """Test error handling in natural language parsing."""

    def test_unparseable_input(self):
        with pytest.raises(ValueError, match="Could not parse"):
            convert_natural("this is gibberish")

    def test_missing_value(self):
        with pytest.raises(ValueError):
            convert_natural("cups to ml")

    def test_invalid_unit(self):
        with pytest.raises(ValueError):
            convert_natural("2 blorg to ml")
