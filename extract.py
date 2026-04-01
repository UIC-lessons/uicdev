import xml.etree.ElementTree as ET


def get_schema():
    tree = ET.parse("d:/projects/uic_dev/uic_dev.drawio")
    root = tree.getroot()
    mx_root = root.find(".//root")

    tables = {}

    for cell in mx_root.findall("mxCell"):
        style = cell.get("style", "")
        if "shape=table" in style:
            tid = cell.get("id")
            val = cell.get("value", "").replace("&lt;", "<").replace("&gt;", ">")
            if val:
                tables[tid] = {"name": val, "rows": []}

    rows_by_parent = {}
    for cell in mx_root.findall("mxCell"):
        pid = cell.get("parent")
        if pid in tables:
            rid = cell.get("id")
            rows_by_parent[rid] = {"tid": pid, "cols": []}

    for cell in mx_root.findall("mxCell"):
        pid = cell.get("parent")
        if pid in rows_by_parent:
            val = cell.get("value", "").strip()
            # extract text inside div if present
            if "<div" in val:
                import re

                m = re.search(r">([^<]+)<", val)
                if m:
                    val = m.group(1).strip()
            # remove html tags completely
            import re

            val = re.sub("<[^<]+>", "", val).strip()
            rows_by_parent[pid]["cols"].append(val)

    for rid, rdata in rows_by_parent.items():
        cols = [c for c in rdata["cols"] if c and c != "&#xa;"]
        if cols:
            tid = rdata["tid"]
            ctype = ""
            cname = ""
            for c in cols:
                if c in ("PK", "FK"):
                    ctype = c
                elif not cname:
                    cname = c
            if cname:
                tables[tid]["rows"].append((cname, ctype))

    with open("d:/projects/uic_dev/schema.txt", "w", encoding="utf-8") as f:
        for tid, tdata in tables.items():
            f.write(f"Table: {tdata['name']}\n")
            for cname, ctype in tdata["rows"]:
                f.write(f"  - {cname} {ctype}\n")
            f.write("\n")


if __name__ == "__main__":
    get_schema()
    print("Schema written to schema.txt")
