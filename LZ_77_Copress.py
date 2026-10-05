def compress(text, search_size=15, lookahead_size=15):
    result = []
    i = 0
    while i < len(text):
        start = i - search_size
        if start < 0:
            start = 0
        search = text[start:i]
        best_offset = 0
        best_length = 0
        for j in range(len(search)):
            length = 0
            while length < lookahead_size:
                if i + length >= len(text):
                    break
                if j + length >= len(search):
                    break
                if search[j + length]!= text[i + length]:
                    break
                length = length + 1
            if length > best_length:
                best_length = length
                best_offset = len(search) - j
        if i + best_length < len(text):
            next_char = text[i + best_length]
        else:
            next_char = ""
        result.append((best_offset, best_length, next_char))
        i = i + best_length + 1
    return result

filename = input("Enter file name: ")

with open(filename, "r", encoding="ascii", errors="ignore") as f:
    text = f.read()

compressed = compress(text)

print("Original length:", len(text))
print("Number of triples:", len(compressed))
print()

for step, triple in enumerate(compressed, start=1):
    offset = triple[0]
    length = triple[1]
    next_char = triple[2]
    print(step, offset, length, repr(next_char))
