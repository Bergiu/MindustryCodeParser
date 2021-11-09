def load_code(filename: str) -> str:
    with open(filename, "r") as f:
        lines = f.read()
    return lines
