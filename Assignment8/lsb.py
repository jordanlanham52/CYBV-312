import sys
import os
import hashlib
from PIL import Image

def sha256_of_file(path, bufsize=8192):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for blk in iter(lambda: f.read(bufsize), b''):
            h.update(blk)
    return h.hexdigest()

def extract_red_lsb_message(path, max_pixels=4096):
    img = Image.open(path).convert('RGB')
    bits = []
    for i, px in enumerate(img.getdata()):
        if i >= max_pixels:
            break
        bits.append(px[0] & 1)

    raw = bytearray()
    for i in range(0, len(bits), 8):
        chunk = bits[i:i+8]
        if len(chunk) < 8:
            break
        val = sum(bit << (7 - idx) for idx, bit in enumerate(chunk))
        raw.append(val)

    data = bytes(raw)
    trimmed = data.lstrip(b'\x00')
    text = trimmed.split(b'\x00', 1)[0].decode('ascii', errors='ignore')
    if text and not text[0].isalpha():
        text = text[1:]
    return text

def main():
    if len(sys.argv) < 2:
        print(f"Usage: {sys.argv[0]} <file1.tiff> <file2.tiff> ...")
        sys.exit(1)

    print("=== Comparison & Extraction ===\n")
    for p in sys.argv[1:]:
        name = os.path.basename(p)
        print(f"{name}")
        print(f"  SHA-256:       {sha256_of_file(p)}")
        msg = extract_red_lsb_message(p)
        if msg:
            print(f"  Hidden Message: \"{msg}\"")
        else:
            print("  Hidden Message: <none>")
        print()

if __name__ == "__main__":
    main()