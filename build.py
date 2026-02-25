from pathlib import Path
import sys

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
DIST = ROOT / "dist"
ASSETS_SRC = ROOT / "assets"
ASSETS_DIST = DIST / "assets"


def copy_assets():
    ASSETS_DIST.mkdir(parents=True, exist_ok=True)
    if not ASSETS_SRC.exists():
        print("⚠️ assets/ introuvable.")
        return
    for p in ASSETS_SRC.rglob("*"):
        if p.is_file():
            rel = p.relative_to(ASSETS_SRC)
            target = ASSETS_DIST / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(p.read_bytes())


def main():
    data_path = ROOT / "data.yaml"
    if not data_path.exists():
        print("❌ data.yaml introuvable.")
        sys.exit(1)

    data = yaml.safe_load(data_path.read_text(encoding="utf-8")) or {}

    DIST.mkdir(exist_ok=True)
    copy_assets()

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    pages = {
        "index.html": "index.html",
        "realisations.html": "realisations.html",
        "experience.html": "experience.html",
        "formation.html": "formation.html",
        "competences.html": "competences.html",
        "extra.html": "extra.html",
        "contact.html": "contact.html",
    }

    for out_name, tpl_name in pages.items():
        tpl = env.get_template(tpl_name)
        html = tpl.render(**data)
        if not html.strip():
            print(f"❌ Rendu vide: {tpl_name}")
            sys.exit(1)
        (DIST / out_name).write_text(html, encoding="utf-8")
        print(f"✅ Généré: dist/{out_name}")

    print("🎉 Terminé. Lance: cd dist && python -m http.server 8000")


if __name__ == "__main__":
    main()