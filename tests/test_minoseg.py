"""b–c) Refaktorálás és dokumentáció: a kód minőségét ellenőrző tesztek (az óra elején pirosak)."""
import ast
import subprocess
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
FAJLOK = ["riport.py", "segedek.py"]
MAX_SOR = 20


def fa(nev):
    return ast.parse((ROOT / nev).read_text(encoding="utf-8"))


def fuggvenyek(nev):
    return [n for n in ast.walk(fa(nev)) if isinstance(n, (ast.FunctionDef, ast.AsyncFunctionDef))]


@pytest.mark.parametrize("nev", FAJLOK)
def test_nincs_global(nev):
    hely = [n.lineno for n in ast.walk(fa(nev)) if isinstance(n, ast.Global)]
    assert not hely, f"{nev}: global utasítás a(z) {hely} sorban. Adj át paramétert, és térj vissza értékkel!"


@pytest.mark.parametrize("nev", FAJLOK)
def test_rovid_fuggvenyek(nev):
    hosszuak = [f"{f.name} ({f.end_lineno - f.lineno + 1} sor)" for f in fuggvenyek(nev) if f.end_lineno - f.lineno + 1 > MAX_SOR]
    assert not hosszuak, f"{nev}: túl hosszú függvények (legfeljebb {MAX_SOR} sor): {hosszuak}. Bontsd kisebb függvényekre!"


@pytest.mark.parametrize("nev", FAJLOK)
def test_dokumentacio(nev):
    assert ast.get_docstring(fa(nev)), f"{nev}: hiányzik a modul docstringje (a fájl elején)."
    hianyzik = [f.name for f in fuggvenyek(nev) if len(ast.get_docstring(f) or "") < 15]
    assert not hianyzik, f"{nev}: ezekhez a függvényekhez kell docstring: {hianyzik}"


@pytest.mark.parametrize("nev", FAJLOK)
def test_tipusjelolesek(nev):
    hianyzik = [f.name for f in fuggvenyek(nev)
                if f.returns is None or any(a.annotation is None for a in f.args.args)]
    assert not hianyzik, f"{nev}: típusjelölés hiányzik (paraméterek és visszatérési érték): {hianyzik}"


@pytest.mark.parametrize("nev", FAJLOK)
def test_beszedes_nevek(nev):
    t = fa(nev)
    gyujto = {id(n) for c in ast.walk(t) if isinstance(c, ast.comprehension) for n in ast.walk(c.target)}  # [x for x in ...] megengedett
    rovid = sorted({n.id for n in ast.walk(t) if isinstance(n, ast.Name) and isinstance(n.ctx, ast.Store)
                    and len(n.id) == 1 and n.id != "_" and id(n) not in gyujto}
                   | {a.arg for f in fuggvenyek(nev) for a in f.args.args if len(a.arg) == 1 and a.arg != "p"})
    assert not rovid, f"{nev}: egybetűs nevek: {rovid}. Adj beszédes nevet (pl. hivasok, modell, ossz_tokenek)!"


def test_ruff():
    ki = subprocess.run([sys.executable, "-m", "ruff", "check", *FAJLOK, "--output-format", "concise"],
                        cwd=ROOT, capture_output=True, text=True)
    assert ki.returncode == 0, "A ruff hibákat talált (futtasd: ruff check .):\n" + ki.stdout[-3000:]
