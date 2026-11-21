import tempfile
import unittest
from pathlib import Path

from ai_risk_replication.sources import load_source_manifest


class TestSourceManifest(unittest.TestCase):
    def test_project_manifest(self):
        path = Path(__file__).resolve().parents[1] / "config" / "sources_manifest.csv"
        rows = load_source_manifest(path)
        self.assertIn("ai_news_search", {r["id"] for r in rows})
        self.assertIn("ai_web_search", {r["id"] for r in rows})

    def test_duplicate_id_rejected(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "sources.csv"
            path.write_text(
                "id,variable,fournisseur_article,etat,commentaire\n"
                "dup,a,src,TO_VERIFY,a\n"
                "dup,b,src,TO_VERIFY,b\n",
                encoding="utf-8",
            )
            with self.assertRaises(ValueError):
                load_source_manifest(path)


if __name__ == "__main__":
    unittest.main()
