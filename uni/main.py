import sys
import importlib
import pkgutil

import uni.recipes
from uni.recipe import Recipe


def load_recipes() -> dict[str, type[Recipe]]:
    recipes = {}

    for _, module_name, _ in pkgutil.iter_modules(uni.recipes.__path__):
        module = importlib.import_module(f"uni.recipes.{module_name}")

        for obj in module.__dict__.values():
            if (
                isinstance(obj, type)
                and issubclass(obj, Recipe)
                and obj is not Recipe
            ):
                if obj.name in recipes:
                    raise RuntimeError(
                        f"duplicate recipe name: {obj.name}"
                    )
                recipes[obj.name] = obj

    return recipes


def main(argv: list[str]) -> None:
    if len(argv) < 3:
        raise RuntimeError(
            "usage: uni install <package> [package ...]"
        )

    command = argv[1]
    args = argv[2:]

    if command != "install":
        raise RuntimeError(f"unknown command: {command}")

    recipes = load_recipes()

    missing = [name for name in args if name not in recipes]
    if missing:
        raise RuntimeError(
            "unknown packages: " + ", ".join(missing)
        )

    for name in args:
        recipe_cls = recipes[name]
        recipe = recipe_cls()

        print(f"installing {recipe.name} {recipe.version}")
        recipe.install()


if __name__ == "__main__":
    main(sys.argv)
