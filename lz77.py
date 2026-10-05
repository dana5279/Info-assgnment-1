import ast

INPUT_FILE = "file1.txt"
TAGS_FILE = "file2.txt"
OUTPUT_FILE = "file3.txt"


def compress(text, window=100, lookahead=50):
    tags = []
    i = 0
    n = len(text)
    while i < n:
        best_len, best_off = 0, 0
        start = max(0, i - window)
        for j in range(start, i):
            l = 0
            while l < lookahead and i + l < n - 1 and text[j + l] == text[i + l]:
                l += 1
            if l > best_len:
                best_len, best_off = l, i - j
        tags.append((best_off, best_len, text[i + best_len]))
        i += best_len + 1
    return tags


def decompress(tags):
    out = []
    for offset, length, next_char in tags:
        start = len(out) - offset
        for k in range(length):
            out.append(out[start + k])
        out.append(next_char)
    return "".join(out)


def compress_file():
    try:
        with open(INPUT_FILE, "r", encoding="utf-8", newline="") as f:
            text = f.read()
    except FileNotFoundError:
        print(f"Error: {INPUT_FILE} not found.")
        return
    if not text:
        print(f"Error: {INPUT_FILE} is empty.")
        return
    tags = compress(text)
    with open(TAGS_FILE, "w", encoding="utf-8") as f:
        for tag in tags:
            f.write(repr(tag) + "\n")
    print(f"Compressed {INPUT_FILE} -> {TAGS_FILE} ({len(tags)} tags):")
    for tag in tags:
        print(tag)


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


def main():
    while True:
        print("\n===== LZ77 =====")
        print("1. Compress   (file1.txt -> file2.txt)")
        print("2. Decompress (file2.txt -> file3.txt)")
        print("3. Exit")
        choice = input("Choose: ").strip()
        if choice == "1":
            compress_file()
        elif choice == "2":
            decompress_file()
        elif choice == "3":
            break
        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()