#!/usr/bin/env python3
"""news-image-20261122 (v2r): write the front page to /output/entry.png.

The entry image is the front page "THE WORLD TODAY" for Sunday
22 November 2026, rebuilt for the v2r resubmission: hero text left /
picture right, a 2x2 grid of supporting stories, a numbers strip and
a ticker. The picture was composed once (see the builder log) and is
shipped in this repository as entry.png.

This program does no drawing and no network. It checks the embedded
PNG against the competition gate (signature, IHDR first, every chunk
CRC, IEND present, at most 1024x1024, at most 1 MiB, no trailing
bytes) and then copies its bytes unchanged to the output directory,
so repeated runs produce byte-identical files. Python 3 standard
library only.
"""

import binascii
import os
import struct
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SRC = os.path.join(HERE, "entry.png")

MAX_BYTES = 1048576
MAX_SIDE = 1024
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"

# A 1x1 white PNG, used only when the embedded image cannot be read
# or fails validation, so the program still writes a valid PNG.
FALLBACK_PNG = bytes.fromhex(
    "89504e470d0a1a0a0000000d4948445200000001000000010802000000907753de"
    "0000000c4944415478da6360000000020001e221bc330000000049454e44ae426082"
)


def _read_u32(buf, off):
    (value,) = struct.unpack(">I", buf[off:off + 4])
    return value


def check_header(data):
    """Check the signature and the IHDR chunk; return (width, height)."""
    if len(data) < 8 or data[:8] != PNG_MAGIC:
        raise ValueError("not a PNG: bad signature")
    if len(data) > MAX_BYTES:
        raise ValueError("image over the 1 MiB cap: %d bytes" % len(data))
    if len(data) < 8 + 8 + 13 + 4:
        raise ValueError("file too short for an IHDR chunk")
    if data[12:16] != b"IHDR":
        raise ValueError("first chunk is not IHDR")
    (width, height) = struct.unpack(">II", data[16:24])
    if width < 1 or height < 1:
        raise ValueError("non-positive dimensions %dx%d" % (width, height))
    if width > MAX_SIDE or height > MAX_SIDE:
        raise ValueError("image over the 1024x1024 cap: %dx%d"
                         % (width, height))
    return width, height


def check_png(data):
    """Walk every chunk, verifying each CRC, and require a clean IEND.

    Raises ValueError on the first problem found.
    """
    check_header(data)
    pos = 8
    seen_iend = False
    while pos + 8 <= len(data):
        length = _read_u32(data, pos)
        ctype = data[pos + 4:pos + 8]
        body_end = pos + 8 + length
        if length > len(data) - pos - 12:
            raise ValueError("chunk %r runs past the end of the file"
                             % ctype)
        stored = _read_u32(data, body_end)
        actual = binascii.crc32(data[pos + 4:body_end]) & 0xFFFFFFFF
        if stored != actual:
            raise ValueError("bad CRC in chunk %r" % ctype)
        pos = body_end + 4
        if ctype == b"IEND":
            seen_iend = True
            break
    if not seen_iend:
        raise ValueError("no IEND chunk found")
    if pos != len(data):
        raise ValueError("%d trailing bytes after IEND"
                         % (len(data) - pos))


def load_image():
    """Return the embedded bytes after validation, else the fallback."""
    try:
        with open(SRC, "rb") as fh:
            data = fh.read()
        check_png(data)
        return data
    except (OSError, ValueError) as exc:
        print("embedded image unusable (%s); using fallback" % exc,
              file=sys.stderr)
        return FALLBACK_PNG


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    data = load_image()
    with open(target, "wb") as fh:
        fh.write(data)
    print("wrote %s (%d bytes)" % (target, len(data)))


if __name__ == "__main__":
    main()
