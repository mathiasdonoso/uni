from uni.formula import Formula


def load_formula(package_name):
    """Dynamically load a formula by name from formulas/ directory"""
    import importlib.util
    from pathlib import Path

    current_file = Path(__file__).resolve()
    formulas_dir = current_file.parent / "formulas"
    formula_file = formulas_dir / f"{package_name}.py"

    if not formula_file.exists():
        raise Exception(f"Formula not found: {formula_file}")

    spec = importlib.util.spec_from_file_location(
        f"uni.formulas.{package_name}", formula_file
    )

    if spec is None or spec.loader is None:
        raise Exception(f"Failed to load formula: {package_name}")

    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)

    for attr_name in dir(module):
        attr = getattr(module, attr_name)
        if isinstance(attr, type) and issubclass(attr, Formula) and attr != Formula:
            return attr()

    raise Exception(f"No Formula class found in {package_name}.py")
