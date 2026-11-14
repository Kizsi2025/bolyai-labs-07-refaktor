import csv
import sys

d = []
eredmeny = {}


def keszit_riport(f):
    global d, eredmeny
    d = []
    fh = open(f, encoding="utf-8")
    r = csv.reader(fh)
    first = True
    for x in r:
        if first:
            first = False
            continue
        d.append(x)
    fh.close()
    m = {}
    for x in d:
        if x[1] not in m:
            m[x[1]] = []
        m[x[1]].append(x)
    eredmeny = {"osszes": len(d), "modellek": {}}
    for k in sorted(m.keys()):
        l = m[k]
        n = len(l)
        s = 0
        for x in l:
            if x[4] == "1":
                s = s + 1
        t = 0
        for x in l:
            t = t + int(x[3])
        tt = []
        for x in l:
            tt.append(int(x[3]))
        tt.sort()
        i = int(0.9 * (len(tt) - 1))
        p90 = tt[i]
        tok = 0
        for x in l:
            tok = tok + int(x[2])
        if k == "nagyobb":
            ar = tok / 1000 * 2.5
        else:
            ar = tok / 1000 * 0.4
        lassu = 0
        for x in l:
            if int(x[3]) > 900:
                lassu = lassu + 1
        eredmeny["modellek"][k] = {"hivasok": n, "sikeres_arany": round(s / n, 3), "atlag_ms": round(t / n, 1),
                                   "p90_ms": p90, "koltseg_usd": round(ar, 2), "lassu_hivasok": lassu}
    s = 0
    for x in d:
        if x[4] == "1":
            s = s + 1
    eredmeny["sikeres_arany"] = round(s / len(d), 3)
    o = 0
    for k in eredmeny["modellek"]:
        o = o + eredmeny["modellek"][k]["koltseg_usd"]
    eredmeny["koltseg_usd"] = round(o, 2)
    if eredmeny["sikeres_arany"] < 0.8:
        eredmeny["figyelmeztetes"] = "Alacsony a sikeres hívások aránya!"
    else:
        eredmeny["figyelmeztetes"] = ""
    return eredmeny


def szoveges_riport(e):
    s = "Bolyai Labs – havi hívásriport\n"
    s = s + "Összes hívás: " + str(e["osszes"]) + ", sikeres: " + str(round(e["sikeres_arany"] * 100, 1)) + "%\n"
    for k in e["modellek"]:
        x = e["modellek"][k]
        s = s + "- " + k + ": " + str(x["hivasok"]) + " hívás, " + str(round(x["sikeres_arany"] * 100, 1)) + "% sikeres, átlag " + str(x["atlag_ms"]) + " ms, p90 " + str(x["p90_ms"]) + " ms, lassú: " + str(x["lassu_hivasok"]) + ", költség: " + str(x["koltseg_usd"]) + " USD\n"
    s = s + "Teljes költség: " + str(e["koltseg_usd"]) + " USD\n"
    if e["figyelmeztetes"] != "":
        s = s + "FIGYELEM: " + e["figyelmeztetes"] + "\n"
    return s


if __name__ == "__main__":
    if len(sys.argv) > 1:
        f = sys.argv[1]
    else:
        f = "data/hivasok_november.csv"
    print(szoveges_riport(keszit_riport(f)), end="")
