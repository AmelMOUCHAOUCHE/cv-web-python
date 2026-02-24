from pathlib import Path
import sys

import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape
import matplotlib.pyplot as plt

ROOT = Path(__file__).parent
TEMPLATES = ROOT / "templates"
DIST = ROOT / "dist"
ASSETS_SRC = ROOT / "assets"
ASSETS_DIST = DIST / "assets"


def make_skills_chart(data: dict, out_path: Path):
    # On prend quelques compétences (toutes catégories confondues)
    cats = data.get("competences", [])
    flat = []
    for c in cats:
        flat.extend(c.get("items", []))

    if not flat:
        return

    labels = [x.get("name", "") for x in flat][:10]
    values = [int(x.get("level", 0)) for x in flat][:10]

    plt.figure()
    plt.bar(labels, values)
    plt.ylim(0, 100)
    plt.xticks(rotation=25, ha="right")
    plt.tight_layout()
    plt.savefig(out_path, dpi=160)
    plt.close()


def main():
    resume_path = ROOT / "resume.yaml"
    if not resume_path.exists():
        print(f"❌ Fichier introuvable: {resume_path}")
        sys.exit(1)

    data = yaml.safe_load(resume_path.read_text(encoding="utf-8")) or {}

    # Prépare dist/
    DIST.mkdir(exist_ok=True)
    ASSETS_DIST.mkdir(parents=True, exist_ok=True)

    # Copie assets/
    if ASSETS_SRC.exists():
        for p in ASSETS_SRC.glob("*"):
            if p.is_file():
                (ASSETS_DIST / p.name).write_bytes(p.read_bytes())
    else:
        print("⚠️ Dossier assets/ introuvable, je continue quand même.")

    # Graph
    try:
        make_skills_chart(data, ASSETS_DIST / "skills.png")
    except Exception as e:
        print("⚠️ Graph skills.png non généré:", e)

    # Jinja
    if not TEMPLATES.exists():
        print(f"❌ Dossier templates/ introuvable: {TEMPLATES}")
        sys.exit(1)

    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES)),
        autoescape=select_autoescape(["html", "xml"]),
    )

    pages = {
        "index.html": "index.html",
        "experiences.html": "experiences.html",
        "projets.html": "projets.html",
        "competences.html": "competences.html",
        "langues.html": "langues.html",
        "certifications.html": "certifications.html",
        "contact.html": "contact.html",
    }

    for out_name, tpl_name in pages.items():
        tpl = env.get_template(tpl_name)
        html = tpl.render(**data)
        if not html.strip():
            print(f"❌ Rendu vide: {tpl_name}")
            sys.exit(1)
        (DIST / out_name).write_text(html, encoding="utf-8")
        print(f"✅ {out_name} généré")

    print("🎉 Build terminé. Ouvre dist/index.html ou lance un serveur local.")


if __name__ == "__main__":
    main()
