#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from pathlib import Path

STATIC_DIR = Path("worlds_static")
DYNAMIC_DIR = Path("worlds_dynamic")
OUT_DIR = Path("worlds_unified")

N = 200   # number of merged worlds to produce


def indent(elem, level=0):
    """Pretty-print XML for readability."""
    i = "\n" + level*"  "
    if len(elem):
        if not elem.text or not elem.text.strip():
            elem.text = i + "  "
        for child in elem:
            indent(child, level+1)
        if not child.tail or not child.tail.strip():
            child.tail = i
    if level and (not elem.tail or not elem.tail.strip()):
        elem.tail = i


def load_world(path: Path) -> ET.ElementTree:
    try:
        return ET.parse(str(path))
    except Exception:
        with open(path, 'r') as f:
            content = f.read()  

        content = content.replace('<pose frame=>', '<pose>')
        content = content.replace('\\', '')

        return ET.ElementTree(ET.fromstring(content))



def get_world_root(tree: ET.ElementTree) -> ET.Element:
    root = tree.getroot()
    world_elem = root.find("world")
    if world_elem is None:
        raise RuntimeError("[ERROR] SDF missing <world> element")
    return world_elem


def extract_dyn_elements(dyn_world: Path):
    """Extract actors + plugin models from dynamic world."""
    tree = load_world(dyn_world)
    droot = get_world_root(tree)

    dyn_elements = []

    for elem in list(droot):
        tag = elem.tag

        # ignore sun & ground plane
        if tag == "include":
            uri = elem.find("uri")
            if uri is not None and ("sun" in uri.text or "ground" in uri.text):
                continue

        # collect actors and plugin models
        if tag == "actor":
            dyn_elements.append(elem)
        elif tag == "model":
            plugins = elem.findall("plugin")
            if len(plugins) > 0:
                dyn_elements.append(elem)
        elif tag == "plugins":
            dyn_elements.append(elem)

    return dyn_elements


def ensure_unique_name(elem, existing_names):
    n = elem.get("name", "unnamed")
    if n not in existing_names:
        existing_names.add(n)
        return

    base = n
    i = 1
    while True:
        new = f"{base}_{i}"
        if new not in existing_names:
            elem.set("name", new)
            existing_names.add(new)
            return
        i += 1


def compose(static_world, dynamic_world, out_world):
    st_tree = load_world(static_world)
    static_root = get_world_root(st_tree)
    dyn_elems = extract_dyn_elements(dynamic_world)

    existing = set()
    for e in list(static_root):
        if "name" in e.attrib:
            existing.add(e.attrib["name"])

    for elem in dyn_elems:
        elem_copy = ET.fromstring(ET.tostring(elem))
        ensure_unique_name(elem_copy, existing)
        static_root.append(elem_copy)

    indent(st_tree.getroot())
    OUT_DIR.mkdir(exist_ok=True)
    st_tree.write(str(out_world), encoding="utf-8", xml_declaration=True)


def main():
    STATIC_DIR.mkdir(exist_ok=True)
    DYNAMIC_DIR.mkdir(exist_ok=True)
    OUT_DIR.mkdir(exist_ok=True)

    success = 0

    for i in range(1, N+1):
        static_path = STATIC_DIR / f"static_seed_{i:04d}.world"
        dynamic_path = DYNAMIC_DIR / f"dynamic_seed_{i:04d}.world"
        out_path = OUT_DIR / f"unified_seed_{i:04d}.world"

        if not static_path.exists():
            print(f"[WARN] missing static {static_path}, skipping")
            continue
        if not dynamic_path.exists():
            print(f"[WARN] missing dynamic {dynamic_path}, skipping")
            continue

        try:
            compose(static_path, dynamic_path, out_path)
            success += 1
            print(f"[OK] merged {success}/{N}", end="\r")
        except Exception as e:
            print(f"\n[ERROR] merging failed on seed {i}: {e}")

    print(f"\nDone. success={success}/{N}")


if __name__ == "__main__":
    main()

