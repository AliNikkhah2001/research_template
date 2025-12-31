# Datasets

Track dataset manifests, download scripts, and data cards here. Recommended pattern:
- One subfolder per dataset with `summary.md`, `tags.md`, and any loader scripts.
- Keep raw/processed files in storage buckets or DVC; avoid committing large binaries.
- Add checksums or small CSV manifests so others can verify what was used.
