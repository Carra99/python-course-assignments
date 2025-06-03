import sys
import codecs

if len(sys.argv) != 2:
    print("Usage: python rot13_file.py <filename>")
    sys.exit(1)

filename = sys.argv[1]

with open(filename, 'r', encoding='utf-8') as f:
    content = f.read()

rot13_content = codecs.encode(content, 'rot_13')

with open(filename, 'w', encoding='utf-8') as f:
    f.write(rot13_content)

print(f"File '{filename}' has been ROT13 encoded.")
