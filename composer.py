#!/usr/bin/env python3
import xml.etree.ElementTree as ET
from pathlib import Path

STATIC_DIR = Path("worlds_static")
DYNAMIC_DIR = Path("worlds_dynamic")
OUT_DIR = Path("worlds_unified")

N = 200   # number of merged worlds to produce


def collect_xy_from_elems(elems):
    xs, ys = [], []
    for elem in elems:
        if elem.tag not in ("model", "actor"):
            continue
        pose = elem.find("pose")
        if pose is None or not pose.text:
            continue
        vals = pose.text.strip().split()
        if len(vals) < 2:
            continue
        x, y = map(float, vals[:2])
        xs.append(x)
        ys.append(y)
    if not xs:
        return None
    return min(xs), max(xs), min(ys), max(ys)


def world_bounds(world_root: ET.Element):
    """Compute axis-aligned bounds of all models/actors in a world."""
    elems = [e for e in list(world_root) if e.tag in ("model", "actor")]
    return collect_xy_from_elems(elems)


def indent(elem, level=0):
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
    #Extract actors + plugin models from dynamic world
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
            dyn_elements.append(elem)
        elif tag == "plugins":
            dyn_elements.append(elem)
            
    dyn_bounds = collect_xy_from_elems(dyn_elements)
    return dyn_elements, dyn_bounds


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


def translate_model(elem, dx, dy, dz):
    pose = elem.find("pose")
    if pose is not None and pose.text:
        vals = pose.text.strip().split()
        if len(vals) >= 6:
            x, y, z, roll, pitch, yaw = map(float, vals)
            x += dx
            y += dy
            z += dz
            pose.text = f"{x} {y} {z} {roll} {pitch} {yaw}"
    return elem


def compose(static_world, dynamic_world, out_world):
    st_tree = load_world(static_world)
    static_root = get_world_root(st_tree)

    dyn_elems, dyn_bounds = extract_dyn_elements(dynamic_world)

    static_bounds = world_bounds(static_root)

    gap = 0.3

    if static_bounds and dyn_bounds:
        sminx, smaxx, sminy, smaxy = static_bounds
        dminx, dmaxx, dminy, dmaxy = dyn_bounds

        offset_x = (smaxx + gap) - dminx
        static_cy = 0.5 * (sminy + smaxy)
        dyn_cy = 0.5 * (dminy + dmaxy)
        offset_y  = static_cy - dyn_cy
    else:
        print("[WARN] Failed to compute bounds, using default offset (6,0,0)")

    
    existing = set()
    for e in list(static_root):
        if "name" in e.attrib:
            existing.add(e.attrib["name"])

    for elem in dyn_elems:
        elem_copy = ET.fromstring(ET.tostring(elem))
        translate_model(elem_copy, offset_x, offset_y, offset_z)
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

