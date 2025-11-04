"""Recipe scaling utility."""

from typing import Any


def scale_recipe(recipe: dict[str, Any], new_servings: int) -> dict[str, Any]:
    """
    Scale a recipe to a different number of servings.

    Args:
        recipe: Recipe dictionary with 'servings' and 'ingredients' keys
        new_servings: Target number of servings

    Returns:
        New recipe dictionary with scaled ingredient amounts

    Example:
        recipe = {
            "servings": 4,
            "ingredients": [
                {"amount": 2, "unit": "cups", "name": "flour"},
                {"amount": 1, "unit": "tsp", "name": "salt"},
            ]
        }
        scaled = scale_recipe(recipe, 8)
        # Returns recipe with doubled amounts
    """
    if "servings" not in recipe:
        raise ValueError("Recipe must have 'servings' key")
    if "ingredients" not in recipe:
        raise ValueError("Recipe must have 'ingredients' key")

    original_servings = recipe["servings"]
    if original_servings <= 0:
        raise ValueError("Original servings must be positive")
    if new_servings <= 0:
        raise ValueError("New servings must be positive")

    scale_factor = new_servings / original_servings

    # Create a copy of the recipe
    scaled_recipe = {
        "servings": new_servings,
        "ingredients": [],
    }

    # Copy any additional keys
    for key, value in recipe.items():
        if key not in ["servings", "ingredients"]:
            scaled_recipe[key] = value

    # Scale each ingredient
    for ingredient in recipe["ingredients"]:
        scaled_ingredient = ingredient.copy()
        if "amount" in ingredient:
            scaled_ingredient["amount"] = ingredient["amount"] * scale_factor
        scaled_recipe["ingredients"].append(scaled_ingredient)

    return scaled_recipe
