# Code

Modularize experiments, pipelines, and libraries here. Suggested workflow:
- Create one subfolder per module or pipeline (e.g., `code/baseline-model`).
- Add a short `summary.md` and `tags.md` so the README generator can surface it.
- Keep heavy assets (checkpoints, datasets) out of git; prefer releases or cloud storage.
- Include a `README.md` or usage script inside each module for reproducibility.
