# Research Project Template

Reusable skeleton for organizing research code, datasets, models, evaluation, and literature.
_Last updated: 2025-12-31 10:05 UTC_

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
- [ ] **Example Baseline Module** (`code/example-project`) — tags: template, example, baseline
  - A placeholder module that shows how to document code entries. Include setup steps, expected inputs/outputs, and a pointer to scripts or notebooks inside this folder.

## Datasets
- [ ] **Example Dataset Card** (`datasets/example-dataset`) — tags: template, example, manifest
  - Document how to fetch the data (e.g., scripts, buckets, DOIs) and include schema highlights or licensing notes. Keep large files out of git; use manifests instead.

## Papers
- [ ] **Example Paper Note** (`papers/example-paper`) — tags: template, review
  - Use this file to jot down key contributions, datasets, and open questions. This keeps the main README concise while still surfacing what you have read.

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
