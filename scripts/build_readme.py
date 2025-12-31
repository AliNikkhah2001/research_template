#!/usr/bin/env python3
import json
import re
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROJECT_FILE = ROOT / "project.json"

DEFAULT_META = {
    "name": "Research Project Template",
    "description": "A lightweight scaffold for organizing research code, datasets, experiments, and literature notes.",
    "homepage": "",
}

CHECKBOX_RE = re.compile(r"^[#>*-]?\s*\[([ xX])\]\s*(.*)$")


def load_project_meta() -> dict:
    meta = DEFAULT_META.copy()
    if PROJECT_FILE.exists():
        try:
            loaded = json.loads(PROJECT_FILE.read_text())
            if isinstance(loaded, dict):
                meta.update({k: v for k, v in loaded.items() if v is not None})
        except json.JSONDecodeError:
            pass
    return meta


def extract_status(lines: list[str]) -> str:
    for line in lines:
        match = CHECKBOX_RE.match(line.strip())
        if match:
            return "[x]" if match.group(1).lower() == "x" else "[ ]"
    return ""


def parse_summary(summary_path: Path, fallback: str = "") -> tuple[str, str, str]:
    if not summary_path.exists():
        return fallback or summary_path.parent.name, "", ""

    lines = [line.rstrip() for line in summary_path.read_text().splitlines()]
    status = extract_status(lines)

    title = fallback or summary_path.parent.name
    snippet_lines: list[str] = []
    saw_title = False
    for line in lines:
        text = line.strip()
        if not text:
            if saw_title and snippet_lines:
                break
            continue
        if CHECKBOX_RE.match(text):
            continue
        if text.startswith("#"):
            text = text.lstrip("#").strip()
        if not saw_title:
            title = text or title
            saw_title = True
            continue
        snippet_lines.append(text)

    snippet = " ".join(snippet_lines).strip()
    return title, snippet, status


def load_status(folder: Path, fallback: str = "") -> str:
    status_path = folder / "status.md"
    if status_path.exists():
        status = extract_status(status_path.read_text().splitlines())
        if status:
            return status
    return fallback


def parse_tags(tags_path: Path) -> list[str]:
    if not tags_path.exists():
        return []
    return [line.strip() for line in tags_path.read_text().splitlines() if line.strip()]


def collect_entries(base: Path) -> list[dict]:
    entries: list[dict] = []
    if not base.exists():
        return entries
    for folder in sorted(base.iterdir()):
        if not folder.is_dir() or folder.name.startswith("."):
            continue
        title, snippet, status = parse_summary(folder / "summary.md", folder.name)
        entries.append(
            {
                "title": title,
                "slug": folder.name,
                "snippet": snippet,
                "tags": parse_tags(folder / "tags.md"),
                "status": load_status(folder, status),
            }
        )
    return entries


def collect_text_blocks(base: Path) -> list[str]:
    blocks = []
    if not base.exists():
        return blocks
    for path in sorted(base.glob("*.md")):
        if path.name.lower() == "readme.md":
            continue
        title = path.stem.replace("-", " ").title()
        rel_path = path.relative_to(ROOT)
        blocks.append(f"{title} ({rel_path})")
    return blocks


def render_entry_lines(entries: list[dict], base_slug: str, empty_hint: str) -> list[str]:
    lines: list[str] = []
    if entries:
        for entry in entries:
            tags = ", ".join(entry["tags"]) if entry["tags"] else "no tags"
            status = entry["status"] or "[ ]"
            lines.append(f"- {status} **{entry['title']}** (`{base_slug}/{entry['slug']}`) — tags: {tags}")
            if entry["snippet"]:
                lines.append(f"  - {entry['snippet']}")
    else:
        lines.append(f"- {empty_hint}")
    lines.append("")
    return lines


def build_readme() -> str:
    meta = load_project_meta()
    code_entries = collect_entries(ROOT / "code")
    datasets = collect_entries(ROOT / "datasets")
    papers = collect_entries(ROOT / "papers")
    models = collect_text_blocks(ROOT / "models")
    evaluations = collect_text_blocks(ROOT / "evaluation")
    ideas = collect_text_blocks(ROOT / "ideas")
    trainings = collect_text_blocks(ROOT / "training")

    lines: list[str] = []
    lines.append(f"# {meta['name']}")
    lines.append("")
    lines.append(meta["description"])
    lines.append(f"_Last updated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M %Z')}_")
    lines.append("")
    if meta.get("homepage"):
        lines.append(f"Project homepage: {meta['homepage']}")
        lines.append("")

    lines.append("## What this template includes")
    lines.append("- Opinionated folder layout for code, datasets, papers, models, and experiments.")
    lines.append("- Metadata-first README generator (`scripts/build_readme.py`).")
    lines.append("- Optional GitHub Actions to auto-refresh README and Pages.")
    lines.append("- Space for notes, TODOs, and evaluation summaries without cluttering the root README.")
    lines.append("")

    lines.append("## Structure")
    lines.append("- `code/`: experiments, pipelines, and libraries")
    lines.append("- `datasets/`: dataset manifests, download scripts, and notes")
    lines.append("- `papers/`: literature summaries and (optional) PDFs")
    lines.append("- `training/`: reproducible training pipelines and configs")
    lines.append("- `models/`: lightweight model cards and release links")
    lines.append("- `evaluation/`: benchmarks, metrics, and analysis notebooks")
    lines.append("- `ideas/`: backlog items, design docs, and hypotheses")
    lines.append("- `scripts/`: automation such as the README generator")
    lines.append("")

    lines.append("## Code modules")
    lines.extend(
        render_entry_lines(
            code_entries,
            "code",
            "Add a folder like `code/your-module` with `summary.md` + `tags.md`.",
        )
    )

    lines.append("## Datasets")
    lines.extend(
        render_entry_lines(
            datasets,
            "datasets",
            "Track datasets with manifest files instead of raw data.",
        )
    )

    lines.append("## Papers")
    lines.extend(
        render_entry_lines(
            papers,
            "papers",
            "Summarize the papers you have read to keep the literature visible.",
        )
    )

    lines.append("## Models & Training")
    if trainings or models:
        for entry in trainings + models:
            lines.append(f"- {entry}")
        lines.append("")
    else:
        lines.append("- Document experiment configs and link to checkpoints or releases.")
        lines.append("")

    lines.append("## Evaluation")
    if evaluations:
        for entry in evaluations:
            lines.append(f"- {entry}")
        lines.append("")
    else:
        lines.append("- Add benchmark summaries, result tables, or notebooks here.")
        lines.append("")

    lines.append("## Ideas & TODOs")
    if ideas:
        for entry in ideas:
            lines.append(f"- {entry}")
        lines.append("")
    else:
        lines.append("- Capture design docs, hypotheses, and next steps in `ideas/`.")
        lines.append("")

    lines.append("## Using this template")
    lines.append("1) Edit `project.json` with your project name/description.")
    lines.append("2) Add code/dataset/paper folders with `summary.md`, `tags.md`, and optional `status.md` checkboxes.")
    lines.append("3) Run `python3 scripts/build_readme.py` to regenerate `README.md` and `docs/index.md`.")
    lines.append("4) Commit your changes; GitHub Actions will refresh the docs on push.")
    lines.append("")
    lines.append("The generator keeps the README short while surfacing progress across modules, datasets, and readings.")
    lines.append("")

    return "\n".join(lines)


def main() -> None:
    readme_path = ROOT / "README.md"
    content = build_readme()
    readme_path.write_text(content)
    docs_dir = ROOT / "docs"
    docs_dir.mkdir(exist_ok=True)
    docs_path = docs_dir / "index.md"
    docs_path.write_text("---\nlayout: default\n---\n\n" + content)


if __name__ == "__main__":
    main()
