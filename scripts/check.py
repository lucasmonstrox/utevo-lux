"""Validate the distributable package: python scripts/check.py (stdlib only)."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PLUGIN = ROOT / "plugins" / "utevo-lux"
SKILLS = PLUGIN / "skills"
NAMES = {"hi", "exiva", "pl", "hunt", "bug", "look", "exura"}


def check():
    versions = set()
    for agent in ("claude", "codex", "cursor"):
        manifest = json.loads((PLUGIN / f".{agent}-plugin/plugin.json").read_text(encoding="utf-8"))
        assert manifest["name"] == PLUGIN.name
        assert re.fullmatch(r"\d+\.\d+\.\d+", manifest["version"])
        assert (PLUGIN / manifest["skills"]).resolve() == SKILLS
        versions.add(manifest["version"])
        marketplace_path = ".agents/plugins" if agent == "codex" else f".{agent}-plugin"
        catalog = json.loads((ROOT / marketplace_path / "marketplace.json").read_text(encoding="utf-8"))
        assert catalog["name"] == "utevo-lux"
        assert len(catalog["plugins"]) == 1
        entry = catalog["plugins"][0]
        source = entry["source"]["path"] if agent == "codex" else entry["source"]
        assert entry["name"] == "utevo-lux" and (ROOT / source).resolve() == PLUGIN
        if "version" in entry:
            versions.add(entry["version"])
    assert len(versions) == 1, "Plugin and catalog versions differ"
    assert {p.name for p in SKILLS.iterdir() if p.is_dir()} == NAMES

    for name in sorted(NAMES):
        folder = SKILLS / name
        text = (folder / "SKILL.md").read_text(encoding="utf-8")
        assert text.startswith("---\n")
        frontmatter, body = text[4:].split("\n---\n", 1)
        assert f"name: {name}" in frontmatter.splitlines(), name
        assert re.search(r"^description: \S.+", frontmatter, re.MULTILINE), name
        assert "\x00" not in text and "$ARGUMENTS" not in body and "!`" not in body
        for path in folder.rglob("*.md"):
            content = path.read_text(encoding="utf-8")
            assert not re.search(r"Marketero|marketero|\.claude/skills/|bun run features|model: sonnet", content), path
            for target in re.findall(r"\]\(([^)]+)\)", content):
                if target.startswith(("https://", "http://", "#", "<")):
                    continue
                resolved = (path.parent / target.split("#")[0]).resolve()
                assert resolved.is_relative_to(folder), f"Reference outside skill: {path}: {target}"
                assert resolved.is_file(), f"Missing reference: {path}: {target}"
        print(f"OK {name}")

    assert (SKILLS / "look/references/github-pr.md").read_bytes() == (SKILLS / "exura/references/github-pr.md").read_bytes()
    assert (PLUGIN / "assets/logo.png").read_bytes().startswith(b"\x89PNG\r\n\x1a\n")
    readme = (ROOT / "README.md").read_text(encoding="utf-8")
    for target in re.findall(r'(?:\]\(|src=")([^\s)"#]+)', readme):
        if not target.startswith(("https://", "http://")):
            assert (ROOT / target).is_file(), f"README link missing: {target}"
    print("OK manifests, catalogs, references and logo")


if __name__ == "__main__":
    check()
