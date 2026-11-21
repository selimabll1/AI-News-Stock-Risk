"""Print the current metadata inventory; no network request and no mock data."""
from pathlib import Path
from ai_risk_replication.sources import load_source_manifest


def main() -> None:
    manifest = Path(__file__).resolve().parents[1] / "config" / "sources_manifest.csv"
    rows = load_source_manifest(manifest)
    print(f"Source entries: {len(rows)}")
    for row in rows:
        print(f"  {row['id']:<16} {row['etat']:<17} {row['fournisseur_article']}")
    print("Metadata only: no source accessibility has been established by this script.")


if __name__ == "__main__":
    main()
