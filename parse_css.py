def get_blocks():
    with open("style_dump.css") as f:
        lines = f.readlines()
        
    ns = "#purelane-combos-{{ section.id }}"
    out = [f"<style>\n{ns} {{"]
    
    # 1. Grab all :root vars
    in_root = False
    for line in lines:
        if ":root{" in line or ":root {" in line:
            in_root = True
            continue
        if in_root and "}" in line:
            in_root = False
            continue
        if in_root:
            out.append("  " + line.strip())

    # 2. Add some defaults
    out.extend([
        "  padding: clamp(40px, 6vw, 80px) 0;",
        "}",
        f"{ns} a {{ text-decoration: none; }}",
        f"{ns} p, {ns} h2, {ns} h3 {{ margin: 0; }}",
        f"{ns} .wrap {{ max-width: 1200px; margin: 0 auto; padding: 0 18px; }}"
    ])
    
    # 3. Grab classes
    # We want these exactly, but prefixed with our namespace
    classes_to_namespace = [
        ".d2", ".lede", ".kicker", ".rule", ".btn", ".glass", ".comborail", ".combo",
        ".stack", ".swipecue", ".railnote", ".pimg", ".p-combo2", ".p-dish", ".p-eraser",
        ".p-floor", ".p-handwash", ".p-kbtl", ".p-kitchen", ".p-laundry", ".p-mbtl",
        ".p-metal", ".p-tap", ".p-tbtl", ".p-toilet", ".p-wm", ".tier"
    ]
    
    # Simple line-by-line processor for single-line CSS rules (which this file is)
    for line in lines:
        stripped = line.strip()
        if not stripped or stripped.startswith("/*"): continue
        
        # Check if line defines one of our classes
        for cls in classes_to_namespace:
            if stripped.startswith(cls):
                # Replace comma-separated selectors (e.g. .tier .tag,.combo .prow em)
                parts = stripped.split("{")
                if len(parts) == 2:
                    selectors = parts[0].split(",")
                    new_selectors = []
                    for sel in selectors:
                        # only namespace if it starts with .
                        sel = sel.strip()
                        if sel.startswith("."):
                            new_selectors.append(f"{ns} {sel}")
                        else:
                            new_selectors.append(f"{ns} {sel}")
                    
                    new_line = ",".join(new_selectors) + "{" + parts[1]
                    out.append(new_line)
                break
                
    out.append("</style>")
    
    with open("combos-style.liquid", "w") as f:
        f.write("\n".join(out))

get_blocks()
