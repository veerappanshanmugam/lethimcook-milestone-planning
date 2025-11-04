"""Tests for recipe scaling functionality."""

import pytest
from pydantic import ValidationError
from lethimcook import Ingredient, Recipe, scale_recipe


class TestRecipeScaling:
    """Test recipe scaling functionality."""

    def test_double_recipe(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour"),
                Ingredient(amount=1, unit="tsp", name="salt"),
            ]
        )
        scaled = scale_recipe(recipe, 8)

        assert scaled.servings == 8
        assert len(scaled.ingredients) == 2
        assert scaled.ingredients[0].amount == 4
        assert scaled.ingredients[1].amount == 2

    def test_halve_recipe(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour"),
                Ingredient(amount=4, unit="tbsp", name="butter"),
            ]
        )
        scaled = scale_recipe(recipe, 2)

        assert scaled.servings == 2
        assert scaled.ingredients[0].amount == 1
        assert scaled.ingredients[1].amount == 2

    def test_scale_to_odd_number(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour"),
            ]
        )
        scaled = scale_recipe(recipe, 6)

        assert scaled.servings == 6
        assert scaled.ingredients[0].amount == 3

    def test_fractional_scaling(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=3, unit="cups", name="flour"),
            ]
        )
        scaled = scale_recipe(recipe, 3)

        assert scaled.servings == 3
        assert abs(scaled.ingredients[0].amount - 2.25) < 0.01

    def test_preserve_ingredient_properties(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour", note="all-purpose"),
            ]
        )
        scaled = scale_recipe(recipe, 8)

        assert scaled.ingredients[0].unit == "cups"
        assert scaled.ingredients[0].name == "flour"
        assert scaled.ingredients[0].note == "all-purpose"

    def test_ingredient_without_amount(self):
        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(unit="pinch", name="salt"),
            ]
        )
        scaled = scale_recipe(recipe, 8)

        assert scaled.ingredients[0].unit == "pinch"
        assert scaled.ingredients[0].name == "salt"

    def test_preserve_additional_recipe_fields(self):
        recipe = Recipe(
            servings=4,
            name="Chocolate Chip Cookies",
            prep_time="15 minutes",
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour"),
            ]
        )
        scaled = scale_recipe(recipe, 8)

        assert scaled.name == "Chocolate Chip Cookies"
        assert scaled.prep_time == "15 minutes"

    def test_empty_ingredients_list(self):
        recipe = Recipe(
            servings=4,
            ingredients=[]
        )
        scaled = scale_recipe(recipe, 8)

        assert scaled.servings == 8
        assert len(scaled.ingredients) == 0


class TestRecipeScalingErrors:
    """Test error handling in recipe scaling."""

    def test_missing_servings(self):
        with pytest.raises(ValidationError):
            Recipe(
                ingredients=[
                    Ingredient(amount=2, unit="cups", name="flour"),
                ]
            )

    def test_missing_ingredients(self):
        with pytest.raises(ValidationError):
            Recipe(servings=4)

    def test_zero_servings(self):
        with pytest.raises(ValidationError):
            Recipe(
                servings=0,
                ingredients=[]
            )

    def test_negative_servings(self):
        recipe = Recipe(
            servings=4,
            ingredients=[]
        )
        with pytest.raises(ValueError, match="positive"):
            scale_recipe(recipe, -2)
