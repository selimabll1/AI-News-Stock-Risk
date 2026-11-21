"""Read source metadata, not actual licensed observations."""
from csv import DictReader
from pathlib import Path

REQUIRED_COLUMNS = {"id", "variable", "fournisseur_article", "etat", "commentaire"}


def load_source_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8-sig", newline="") as stream:
        reader = DictReader(stream)
        missing = REQUIRED_COLUMNS - set(reader.fieldnames or [])
        if missing:
            raise ValueError(f"Missing columns in source manifest: {sorted(missing)}")
        rows = list(reader)
    if not rows:
        raise ValueError("Source manifest is empty")
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise ValueError("Duplicated source IDs")
    return rows
