import ast

INPUT_FILE = "file1.txt"
TAGS_FILE = "file2.txt"
OUTPUT_FILE = "file3.txt"


def decompress(tags):
    out = []
    for offset, length, next_char in tags:
        start = len(out) - offset
        for k in range(length):
            out.append(out[start + k])
        out.append(next_char)
    return "".join(out)


def decompress_file():
    try:
        with open(TAGS_FILE, "r", encoding="utf-8") as f:
            tags = [ast.literal_eval(line) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Error: {TAGS_FILE} not found. Compress first.")
        return
    text = decompress(tags)
    with open(OUTPUT_FILE, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    print(f"Decompressed {TAGS_FILE} -> {OUTPUT_FILE}")
    try:
        with open(INPUT_FILE, "r", encoding="utf-8", newline="") as f:
            print("Matches original:", f.read() == text)
    except FileNotFoundError:
        pass


