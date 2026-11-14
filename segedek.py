"""Kis segédfüggvények a hívásriporthoz."""


def percentilis(ertekek: list[float], p: float) -> float:
    """A p-edik percentilis a legközelebbi alsó rangszámmal.

    Az értékeket növekvő sorba rendezzük, és az int(p / 100 * (n - 1)) indexű elemet adjuk vissza.
    Példa: percentilis([5, 1, 3, 2, 4], 90) == 4.
    """
    # TODO: írd meg kódkiegészítéssel (a docstring alapján az asszisztens javasol – te ellenőrzöd)
    raise NotImplementedError


def szazalek(arany: float) -> str:
    """Egy 0 és 1 közötti arányt százalékos szöveggé alakít, egy tizedesjegyre kerekítve.

    Példa: szazalek(0.711) == "71.1%".
    """
    # TODO: írd meg kódkiegészítéssel
    raise NotImplementedError
