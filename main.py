import LZ_77
import LZ_77_compressed

print("1. Compression")
print("2. Decompression")

choice = input("Enter your choice: ")

if choice == "1":
    filename = input("Enter file name: ")

    with open(filename, "r", encoding="ascii", errors="ignore") as f:
        text = f.read()

    compressed = LZ_77_compressed.compress(text)

    with open("file2.txt", "w", encoding="utf-8") as f:
        for triple in compressed:
            f.write(str(triple) + "\n")

    print("Compression completed.")

elif choice == "2":
    LZ_77.decompress_file()

else:
    print("Invalid choice.")
