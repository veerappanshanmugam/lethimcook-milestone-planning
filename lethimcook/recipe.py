"""Recipe scaling utility."""

from pydantic import BaseModel, ConfigDict, Field, field_validator


class Ingredient(BaseModel):
    """A recipe ingredient."""
    amount: float | None = None
    unit: str
    name: str
    note: str | None = None

    model_config = ConfigDict(extra="allow")


class Recipe(BaseModel):
    """A recipe with servings and ingredients."""
    servings: int = Field(gt=0)
    ingredients: list[Ingredient]
    name: str | None = None
    prep_time: str | None = None

    model_config = ConfigDict(extra="allow")

    @field_validator("servings")
    @classmethod
    def servings_must_be_positive(cls, v: int) -> int:
        if v <= 0:
            raise ValueError("Servings must be positive")
        return v


def scale_recipe(recipe: Recipe, new_servings: int) -> Recipe:
    """
    Scale a recipe to a different number of servings.

    Args:
        recipe: Recipe object with servings and ingredients
        new_servings: Target number of servings

    Returns:
        New Recipe object with scaled ingredient amounts

    Example:
        from lethimcook.recipe import Recipe, Ingredient

        recipe = Recipe(
            servings=4,
            ingredients=[
                Ingredient(amount=2, unit="cups", name="flour"),
                Ingredient(amount=1, unit="tsp", name="salt"),
            ]
        )
        scaled = scale_recipe(recipe, 8)
    """
    if new_servings <= 0:
        raise ValueError("New servings must be positive")

    scale_factor = new_servings / recipe.servings

    # Scale each ingredient
    scaled_ingredients = []
    for ingredient in recipe.ingredients:
        ingredient_dict = ingredient.model_dump()
        if ingredient.amount is not None:
            ingredient_dict["amount"] = ingredient.amount * scale_factor
        scaled_ingredients.append(Ingredient(**ingredient_dict))

    # Create new recipe with scaled ingredients
    recipe_dict = recipe.model_dump(exclude={"servings", "ingredients"})
    recipe_dict["servings"] = new_servings
    recipe_dict["ingredients"] = scaled_ingredients

    return Recipe(**recipe_dict)
