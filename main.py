#!/usr/bin/env python3
"""news-image-20261122: write the front page to /output/entry.png.

The entry image is the front page "THE WORLD TODAY" for Sunday
22 November 2026, drawn once and shipped with this repository.
This program only validates the embedded PNG and copies its bytes
to the output directory, so two runs write byte-identical files.
Standard library only, no network.
"""

import binascii
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

PNG_SIGNATURE = b"\x89PNG\r\n\x1a\n"

# A 1x1 white PNG, used only if the embedded image is missing or broken.
FALLBACK_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d4948445200000001000000010802000000907753de"
    "0000000c4944415478da6360000000020001e221bc330000000049454e44ae426082"
)


def check_png(data):
    """Walk the PNG chunks, verifying structure and every CRC.

    Also enforces the competition gate: at most 1024x1024 pixels and
    at most 1 MiB, so a bad embedded image fails loudly here instead
    of silently shipping an entry the gate would refuse.

    Raises ValueError on the first problem found.
    """
    if len(data) > 1048576:
        raise ValueError("image exceeds the 1 MiB cap (%d bytes)" % len(data))
    if len(data) < 8 or data[:8] != PNG_SIGNATURE:
        raise ValueError("not a PNG (bad signature)")
    pos = 8
    first = True
    saw_iend = False
    while pos + 8 <= len(data):
        (length,) = struct.unpack(">I", data[pos:pos + 4])
        ctype = data[pos + 4:pos + 8]
        if length > len(data) - pos - 12:
            raise ValueError("chunk %r overruns the file" % ctype)
        if first:
            if ctype != b"IHDR":
                raise ValueError("IHDR must be the first chunk")
            (width, height) = struct.unpack(">II", data[pos + 8:pos + 16])
            if width <= 0 or height <= 0:
                raise ValueError("non-positive image dimensions")
            if width > 1024 or height > 1024:
                raise ValueError(
                    "image exceeds the 1024x1024 cap (%dx%d)" % (width, height))
            first = False
        chunk_end = pos + 8 + length
        (stored_crc,) = struct.unpack(">I", data[chunk_end:chunk_end + 4])
        actual_crc = binascii.crc32(data[pos + 4:chunk_end]) & 0xFFFFFFFF
        if stored_crc != actual_crc:
            raise ValueError("bad CRC in chunk %r" % ctype)
        pos = chunk_end + 4
        if ctype == b"IEND":
            saw_iend = True
            break
    if first:
        raise ValueError("no chunks after the signature")
    if not saw_iend:
        raise ValueError("missing IEND chunk")
    if pos != len(data):
        raise ValueError("trailing bytes after IEND")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    try:
        with open(SRC, "rb") as fh:
            data = fh.read()
        check_png(data)
    except (OSError, ValueError) as exc:
        print("embedded image unusable (%s); writing fallback" % exc,
              file=sys.stderr)
        data = FALLBACK_PNG
    with open(target, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes)" % (target, len(data)))


if __name__ == "__main__":
    main()
