---
layout: default
---

# research_template

Starter skeleton to organize code, datasets, experiments, models, and literature for any research project.
_Last updated: 2025-12-31 15:12 UTC_

Project homepage: https://github.com/AliNikkhah2001/research_template

## What this template includes
- Opinionated folder layout for code, datasets, papers, models, and experiments.
- Metadata-first README generator (`scripts/build_readme.py`).
- Optional GitHub Actions to auto-refresh README and Pages.
- Space for notes, TODOs, and evaluation summaries without cluttering the root README.

## Structure
- `code/`: experiments, pipelines, and libraries
- `datasets/`: dataset manifests, download scripts, and notes
- `papers/`: literature summaries and (optional) PDFs
- `training/`: reproducible training pipelines and configs
- `models/`: lightweight model cards and release links
- `evaluation/`: benchmarks, metrics, and analysis notebooks
- `ideas/`: backlog items, design docs, and hypotheses
- `scripts/`: automation such as the README generator

## Code modules
- [ ] **Starter Module** (`code/starter-module`) — tags: template, starter, module
  - Use this as a pattern for your first code drop: include setup instructions, expected inputs/outputs, and links to scripts or notebooks inside this folder. Replace this text with your module description.

## Datasets
- [ ] **Starter Dataset Card** (`datasets/starter-dataset`) — tags: template, starter, dataset
  - Document how to fetch data (scripts, buckets, DOIs), licensing, schema, and checksums. Keep raw files out of git; include manifests or download scripts here instead.

## Papers
- [ ] **Starter Paper Note** (`papers/starter-paper-note`) — tags: template, review, starter
  - Capture citation, key contributions, datasets, methods, and open questions. Link to the DOI instead of embedding PDFs when licensing is unclear.

## Models & Training
- Document experiment configs and link to checkpoints or releases.

## Evaluation
- Add benchmark summaries, result tables, or notebooks here.

## Ideas & TODOs
- Todo (ideas/todo.md)

## Using this template
1) Edit `project.json` with your project name/description.
2) Add code/dataset/paper folders with `summary.md`, `tags.md`, and optional `status.md` checkboxes.
3) Run `python3 scripts/build_readme.py` to regenerate `README.md` and `docs/index.md`.
4) Commit your changes; GitHub Actions will refresh the docs on push.

The generator keeps the README short while surfacing progress across modules, datasets, and readings.
