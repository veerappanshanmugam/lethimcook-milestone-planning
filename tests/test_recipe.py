"""Tests for recipe scaling functionality."""

import pytest
from measure import scale_recipe


class TestRecipeScaling:
    """Test recipe scaling functionality."""

    def test_double_recipe(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
                {"amount": 1, "unit": "tsp", "name": "salt"},
            ]
        }
        scaled = scale_recipe(recipe, 8)

        assert scaled["servings"] == 8
        assert len(scaled["ingredients"]) == 2
        assert scaled["ingredients"][0]["amount"] == 4
        assert scaled["ingredients"][1]["amount"] == 2

    def test_halve_recipe(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
                {"amount": 4, "unit": "tbsp", "name": "butter"},
            ]
        }
        scaled = scale_recipe(recipe, 2)

        assert scaled["servings"] == 2
        assert scaled["ingredients"][0]["amount"] == 1
        assert scaled["ingredients"][1]["amount"] == 2

    def test_scale_to_odd_number(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
            ]
        }
        scaled = scale_recipe(recipe, 6)

        assert scaled["servings"] == 6
        assert scaled["ingredients"][0]["amount"] == 3

    def test_fractional_scaling(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {"amount": 3, "unit": "cups", "name": "flour"},
            ]
        }
        scaled = scale_recipe(recipe, 3)

        assert scaled["servings"] == 3
        assert abs(scaled["ingredients"][0]["amount"] - 2.25) < 0.01

    def test_preserve_ingredient_properties(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {
                    "amount": 2,
                    "unit": "cups",
                    "name": "flour",
                    "note": "all-purpose",
                },
            ]
        }
        scaled = scale_recipe(recipe, 8)

        assert scaled["ingredients"][0]["unit"] == "cups"
        assert scaled["ingredients"][0]["name"] == "flour"
        assert scaled["ingredients"][0]["note"] == "all-purpose"

    def test_ingredient_without_amount(self):
        recipe = {
            "servings": 4,
            "ingredients": [
                {"unit": "pinch", "name": "salt"},
            ]
        }
        scaled = scale_recipe(recipe, 8)

        # Should not crash, just copy the ingredient as-is
        assert scaled["ingredients"][0]["unit"] == "pinch"
        assert scaled["ingredients"][0]["name"] == "salt"

    def test_preserve_additional_recipe_fields(self):
        recipe = {
            "servings": 4,
            "name": "Chocolate Chip Cookies",
            "prep_time": "15 minutes",
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
            ]
        }
        scaled = scale_recipe(recipe, 8)

        assert scaled["name"] == "Chocolate Chip Cookies"
        assert scaled["prep_time"] == "15 minutes"

    def test_empty_ingredients_list(self):
        recipe = {
            "servings": 4,
            "ingredients": []
        }
        scaled = scale_recipe(recipe, 8)

        assert scaled["servings"] == 8
        assert len(scaled["ingredients"]) == 0


class TestRecipeScalingErrors:
    """Test error handling in recipe scaling."""

    def test_missing_servings(self):
        recipe = {
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
            ]
        }
        with pytest.raises(ValueError, match="servings"):
            scale_recipe(recipe, 8)

    def test_missing_ingredients(self):
        recipe = {
            "servings": 4,
        }
        with pytest.raises(ValueError, match="ingredients"):
            scale_recipe(recipe, 8)

    def test_zero_servings(self):
        recipe = {
            "servings": 0,
            "ingredients": []
        }
        with pytest.raises(ValueError, match="positive"):
            scale_recipe(recipe, 4)

    def test_negative_servings(self):
        recipe = {
            "servings": 4,
            "ingredients": []
        }
        with pytest.raises(ValueError, match="positive"):
            scale_recipe(recipe, -2)
