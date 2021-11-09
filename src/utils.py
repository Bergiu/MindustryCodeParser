def load_code(filename: str) -> str:
    with open(filename, "r") as f:
        lines = f.read()
    return lines


def write_code(filename: str, text: str):
    with open(filename, "w") as f:
        f.write(text)
