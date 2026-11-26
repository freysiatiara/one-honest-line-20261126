import os

LINE = "You said 'just make it pop' \u2014 I've popped it 47 times now, and it has never once popped."

MAX_CHARS = 200


def resolve_output_path():
    entry_output = os.environ.get("ENTRY_OUTPUT")
    if entry_output:
        return entry_output
    for var in ("OUTPUT_DIR", "MAKEFUN_OUTPUT_DIR"):
        directory = os.environ.get(var)
        if directory:
            return os.path.join(directory, "entry.txt")
    return os.path.join(
        os.path.dirname(os.path.abspath(__file__)), "entry.txt"
    )


def main():
    line = LINE
    if not (1 <= len(line) <= MAX_CHARS) or not line.strip():
        raise SystemExit(
            "entry line must be 1..%d non-blank characters, got %d"
            % (MAX_CHARS, len(line))
        )
    path = resolve_output_path()
    directory = os.path.dirname(path)
    if directory:
        os.makedirs(directory, exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="") as handle:
        handle.write(line)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()
