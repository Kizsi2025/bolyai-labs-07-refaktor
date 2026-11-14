# Bolyai Labs – 7. blokk: Páros programozás géppel (refaktorálási feladat)

## Feladatkártya #7

> Vezető fejlesztőként szeretném, ha a régi hívásriport-szkriptet (`riport.py`) valaki rendbe tenné: ugyanazt csinálja, de olvasható, dokumentált és karbantartható legyen. Az MI-asszisztenst nyugodtan használd – de te felelsz minden soráért.

| Rész | Feladat | Tesztek |
| --- | --- | --- |
| a) | **kódkiegészítés:** a `segedek.py` két függvénye a docstring alapján | `test_segedek.py` |
| b) | **refaktorálás:** a `riport.py` átírása kis, beszédes nevű függvényekre, konstansokkal | `test_viselkedes.py` (végig zöld!), `test_minoseg.py` |
| c) | **dokumentáció:** modul- és függvény-docstringek, típusjelölések | `test_minoseg.py` |
| d) | **AI-napló:** mit fogadtál el, mit utasítottál el, és miért | `test_ai_naplo.py` |

- [ ] saját repó ebből a sablonból (pl. `refaktor-13b-07`, Public), klónozva VS Code-ba
- [ ] virtuális környezet, `pip install -r requirements.txt`
- [ ] az összes teszt zöld helyben (`python -m pytest`) és az Actions fülön (**Feladatkártya 7**)
- [ ] commitok kis lépésekben; az utolsó commitüzenet: `refactor: hívásriport rendbetétele (feladatkártya #7)`
- [ ] a repó linkje beadva a Teams-feladatba

**Érték:** 5 sprintpont (zöld build 2, határidő 1, commitüzenet 1, kilépőkérdések 1). **Határidő:** a 2. óra vége.

## Indulás

```bash
git clone https://github.com/<felhasznalonev>/refaktor-13b-07.git
cd refaktor-13b-07
python -m venv .venv
.venv\Scripts\activate        # Windows  (macOS/Linux: source .venv/bin/activate)
pip install -r requirements.txt
python riport.py               # a régi kód kimenete
python -m pytest               # a viselkedési tesztek zöldek, a minőségiek pirosak
```

## Az aranyszabály

**A `tests/test_viselkedes.py` tesztjeinek végig zöldnek kell maradniuk.** Ezek rögzítik, mit csinál most a riport. Ha egy refaktorálási lépés után pirosak lesznek, az a lépés megváltoztatta a viselkedést: vond vissza (`git restore riport.py`), vagy javítsd. Minden zöld lépés után commitolj.

A teszteket és az `elvart_*` fájlokat ne módosítsd.

## Az IDE-asszisztens

GitHub Copilot: VS Code → Extensions → **GitHub Copilot** → bejelentkezés a GitHub-fiókkal. A Copilot Free bármely GitHub-fiókkal működik (havi kerettel); a diákok a GitHub Education programon keresztül kibővített hozzáférést kaphatnak.

Hasznos kérések a Copilot Chatben (jelöld ki a kódot előtte):
- `/explain` – mit csinál ez a rész?
- „Bontsd ezt a függvényt kisebb, beszédes nevű függvényekre, a viselkedés ne változzon.”
- `/doc` – docstring generálása
- „Cseréld a varázsszámokat (900, 0.8, 2.5, 0.4) nevesített konstansokra.”
