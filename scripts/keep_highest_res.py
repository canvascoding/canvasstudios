#!/usr/bin/env python3
import argparse
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Dict, List, Optional, Tuple

try:
    from PIL import Image
except Exception:
    Image = None

SIZE_SUFFIX_RE = re.compile(r"^(?P<base>.+)-(?P<w>\d+)x(?P<h>\d+)$")
IMAGE_EXTS = {
    ".jpg",
    ".jpeg",
    ".png",
    ".gif",
    ".tif",
    ".tiff",
    ".bmp",
    ".webp",
    ".heic",
    ".heif",
}


@dataclass(frozen=True)
class ImageItem:
    path: Path
    base: str
    size: Optional[Tuple[int, int]]
    file_size: int

    @property
    def area(self) -> Optional[int]:
        if not self.size:
            return None
        return self.size[0] * self.size[1]


def parse_size_from_name(stem: str) -> Tuple[str, Optional[Tuple[int, int]]]:
    match = SIZE_SUFFIX_RE.match(stem)
    if not match:
        return stem, None
    return match.group("base"), (int(match.group("w")), int(match.group("h")))


def get_size_with_pillow(path: Path) -> Optional[Tuple[int, int]]:
    if Image is None:
        return None
    try:
        with Image.open(path) as img:
            return img.size
    except Exception:
        return None


def get_size_with_sips(path: Path) -> Optional[Tuple[int, int]]:
    if sys.platform != "darwin":
        return None
    result = subprocess.run(
        ["sips", "-g", "pixelWidth", "-g", "pixelHeight", str(path)],
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        return None
    width = height = None
    for line in result.stdout.splitlines():
        line = line.strip()
        if "pixelWidth" in line:
            parts = line.split(":")
            if len(parts) == 2 and parts[1].strip().isdigit():
                width = int(parts[1].strip())
        if "pixelHeight" in line:
            parts = line.split(":")
            if len(parts) == 2 and parts[1].strip().isdigit():
                height = int(parts[1].strip())
    if width and height:
        return (width, height)
    return None


def get_image_size(path: Path) -> Optional[Tuple[int, int]]:
    size = get_size_with_pillow(path)
    if size:
        return size
    return get_size_with_sips(path)


def collect_images(root: Path) -> List[ImageItem]:
    items: List[ImageItem] = []
    for entry in root.iterdir():
        if not entry.is_file():
            continue
        if entry.suffix.lower() not in IMAGE_EXTS:
            continue
        base, name_size = parse_size_from_name(entry.stem)
        size: Optional[Tuple[int, int]] = None
        if name_size is None:
            size = get_image_size(entry)
        else:
            size = name_size
            if Image is not None:
                actual = get_size_with_pillow(entry)
                if actual:
                    size = actual
        items.append(
            ImageItem(
                path=entry,
                base=base,
                size=size,
                file_size=entry.stat().st_size,
            )
        )
    return items


def choose_deletions(
    grouped: Dict[str, List[ImageItem]], aggressive: bool
) -> Tuple[List[Path], List[ImageItem]]:
    to_delete: List[Path] = []
    unknown: List[ImageItem] = []

    for _base, items in grouped.items():
        if len(items) <= 1:
            continue
        known = [item for item in items if item.area is not None]
        unknown_items = [item for item in items if item.area is None]
        if not known:
            unknown.extend(unknown_items)
            continue
        best = max(known, key=lambda item: (item.area, item.file_size))
        for item in known:
            if item.path == best.path:
                continue
            to_delete.append(item.path)
        if aggressive:
            for item in unknown_items:
                to_delete.append(item.path)
        else:
            unknown.extend(unknown_items)
    return to_delete, unknown


def format_size(size: Optional[Tuple[int, int]]) -> str:
    if not size:
        return "unknown"
    return f"{size[0]}x{size[1]}"


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Keep only the highest resolution image for each base name."
    )
    parser.add_argument(
        "--dir",
        default="uploads",
        help="Folder to scan (default: uploads)",
    )
    parser.add_argument(
        "--delete",
        action="store_true",
        help="Actually delete files (default: dry-run)",
    )
    parser.add_argument(
        "--aggressive",
        action="store_true",
        help="Also delete files with unknown dimensions when duplicates exist",
    )
    args = parser.parse_args()

    root = Path(args.dir)
    if not root.exists() or not root.is_dir():
        print(f"Directory not found: {root}")
        return 1

    items = collect_images(root)
    if not items:
        print("No images found.")
        return 0

    grouped: Dict[str, List[ImageItem]] = {}
    for item in items:
        grouped.setdefault(item.base, []).append(item)

    to_delete, unknown = choose_deletions(grouped, args.aggressive)

    print(f"Scanned {len(items)} images across {len(grouped)} groups.")
    if unknown and not args.aggressive:
        print(
            f"Skipped {len(unknown)} files with unknown dimensions. "
            "Use --aggressive to include them."
        )
        for item in unknown:
            print(f"  keep (unknown size): {item.path} ({format_size(item.size)})")

    if not to_delete:
        print("No deletions needed.")
        return 0

    action = "Deleting" if args.delete else "Dry run - would delete"
    print(f"{action} {len(to_delete)} files:")
    for path in to_delete:
        print(f"  {path}")
        if args.delete:
            try:
                path.unlink()
            except Exception as exc:
                print(f"  failed: {path} ({exc})")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
