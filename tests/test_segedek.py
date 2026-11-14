"""a) Kódkiegészítés: a segedek.py két függvénye."""
from segedek import percentilis, szazalek


def test_percentilis():
    assert percentilis([5, 1, 3, 2, 4], 90) == 4
    assert percentilis([10, 20, 30, 40, 50, 60, 70, 80, 90, 100], 90) == 90
    assert percentilis([7], 50) == 7
    assert percentilis([3, 1, 2], 0) == 1


def test_szazalek():
    assert szazalek(0.711) == "71.1%"
    assert szazalek(0.984) == "98.4%"
    assert szazalek(1) == "100%" or szazalek(1) == "100.0%"
    assert szazalek(0.437) == "43.7%"
