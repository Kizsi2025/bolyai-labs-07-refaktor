"""d) Az AI-napló kitöltése."""
from pathlib import Path

NAPLO = Path(__file__).resolve().parent.parent / "AI_NAPLO.md"


def test_ai_naplo_kitoltve():
    szoveg = NAPLO.read_text(encoding="utf-8")
    assert "TODO" not in szoveg, "Az AI_NAPLO.md-ben még maradt TODO."
    assert len(szoveg) >= 900, "Az AI-napló túl rövid: minden kérdésre 2–3 mondatban válaszolj."
