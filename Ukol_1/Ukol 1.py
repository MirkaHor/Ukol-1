class Zvire:
    def __init__(self, jmeno: str, druh: str, vaha: int):
        self.jmeno = jmeno
        self.druh = druh
        self.vaha = vaha

    def __str__(self):
        return f"{self.jmeno} ({self.druh}), váha: {self.vaha} kg"

    def export_to_dict(self):
        return {'jmeno': self.jmeno, 'druh': self.druh, 'vaha': self.vaha}

# Test Zvire class
zvire = Zvire('Láďa', 'Koala', 15)
assert hasattr(zvire, 'jmeno')
assert hasattr(zvire, 'druh')
assert hasattr(zvire, 'vaha')
assert isinstance(zvire.jmeno, str)
assert isinstance(zvire.druh, str)
assert isinstance(zvire.vaha, int)
assert zvire.export_to_dict() == {'jmeno': 'Láďa', 'druh': 'Koala', 'vaha': 15}

class Zamestnanec:
    def __init__(self, cele_jmeno: str, rocni_plat: int, pozice: str):
        self.cele_jmeno = cele_jmeno
        self.rocni_plat = rocni_plat
        self.pozice = pozice

    def __str__(self):
        return f"{self.cele_jmeno} ({self.pozice}), roční plat: {self.rocni_plat} Kč"

    def ziskej_inicialy(self):
        jmena = self.cele_jmeno.split()
        return f"{jmena[0][0]}.{jmena[1][0]}."

# Test Zamestnanec class
zamestnanec = Zamestnanec('Petr Novak', 50000, 'Programátor')
assert hasattr(zamestnanec, 'cele_jmeno')
assert hasattr(zamestnanec, 'rocni_plat')
assert hasattr(zamestnanec, 'pozice')
assert isinstance(zamestnanec.cele_jmeno, str)
assert isinstance(zamestnanec.rocni_plat, int)
assert isinstance(zamestnanec.pozice, str)
assert zamestnanec.ziskej_inicialy() == 'P.N.'

class Reditel(Zamestnanec):
    def __init__(self, cele_jmeno: str, rocni_plat: int, oblibene_zvire: Zvire):
        super().__init__(cele_jmeno, rocni_plat, 'Reditel')
        self.oblibene_zvire = oblibene_zvire

# Test Reditel class
zvire = Zvire('Lev', 'Lvice', 150)
reditel = Reditel('Jan Novotny', 80000, zvire)
assert isinstance(reditel.oblibene_zvire, Zvire)

class Zoo:
    def __init__(self, jmeno: str, adresa: str, reditel: Reditel, zamestnanci: list, zvirata: list):
        self.jmeno = jmeno
        self.adresa = adresa
        self.reditel = reditel
        self.zamestnanci = zamestnanci
        self.zvirata = zvirata

    def vaha_vsech_zvirat_v_zoo(self):
        return sum(zvire.vaha for zvire in self.zvirata)

    def mesicni_naklady_na_zamestnance(self):
        platy = sum(zamestnanec.rocni_plat for zamestnanec in self.zamestnanci) + self.reditel.rocni_plat
        return platy / 12

# Test Zoo class
zoo = Zoo('ZOO Praha', 'U Trojského zámku 3/120', reditel, [zamestnanec], [zvire])
assert hasattr(zoo, 'jmeno')
assert hasattr(zoo, 'adresa')
assert hasattr(zoo, 'reditel')
assert hasattr(zoo, 'zamestnanci')
assert hasattr(zoo, 'zvirata')
assert isinstance(zoo.nazev, str)
assert isinstance(zoo.adresa, str)
assert isinstance(zoo.reditel, Reditel)
assert isinstance(zoo.zamestnanci, list)
assert isinstance(zoo.zvirata, list)
assert zoo.vaha_vsech_zvirat_v_zoo() == 150
assert zoo.mesicni_naklady_na_zamestnance() == (zamestnanec.rocni_plat + reditel.rocni_plat) / 12