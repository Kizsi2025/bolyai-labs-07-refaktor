"""A biztonsági háló: a riport viselkedése a refaktorálás után sem változhat.

Ezek a tesztek a régi kód kimenetét rögzítik (karakterizációs tesztek). Az óra elején is zöldek – és végig zöldnek kell maradniuk.
"""
import json
import os
import subprocess
import sys
from pathlib import Path

import pytest

from riport import keszit_riport, szoveges_riport

T = Path(__file__).resolve().parent
ROOT = T.parent


@pytest.mark.parametrize("naplo, elvart", [("data/hivasok_november.csv", "elvart_riport.json"), ("tests/kis_naplo.csv", "elvart_kis.json")])
def test_riport_adatai(naplo, elvart):
    assert keszit_riport(str(ROOT / naplo)) == json.loads((T / elvart).read_text(encoding="utf-8"))


@pytest.mark.parametrize("naplo, elvart", [("data/hivasok_november.csv", "elvart_kimenet.txt"), ("tests/kis_naplo.csv", "elvart_kis_kimenet.txt")])
def test_szoveges_riport(naplo, elvart):
    assert szoveges_riport(keszit_riport(str(ROOT / naplo))) == (T / elvart).read_text(encoding="utf-8")


def test_parancssor():
    ki = subprocess.run([sys.executable, "riport.py"], cwd=ROOT, capture_output=True, text=True, encoding="utf-8",
                        env={**os.environ, "PYTHONIOENCODING": "utf-8"})
    assert ki.returncode == 0, ki.stderr
    assert ki.stdout == (T / "elvart_kimenet.txt").read_text(encoding="utf-8")
