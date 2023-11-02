class Auto: 
    def __init__(self, registracni_znacka: str, typ_vozidla: str, najete_km: int):
        self.registracni_znacka = registracni_znacka
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupne = True
        self.tachometr = 0

    def pujc_auto(self):
      if self.dostupne:
          self.dostupne = False
          return f"Potvrzuji zapůjčení vozidla."
      else:
          return f"Vozidlo není k dispozici."
      
    def get_info(self):
        return f"Registrační značka: {self.registracni_znacka}, typ vozidla: {self.typ_vozidla}, najeté km: {self.najete_km}."
    
    def vrat_auto(self, tachometr: int, pocet_dni: int):
      self.dostupne = True
      self.tachometr += tachometr
      cena = 400 * pocet_dni if pocet_dni < 7 else 300 * pocet_dni
      return f"Děkujeme za vrácení vozidla. Cena půjčení je {cena} Kč."
   
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", 47534)
auto2 = Auto("1P3 4747", "Škoda Octavia", 41253)

uzivatel_pozadovana_znacka = input("Jakou značku vozidla si chcete půjčit? (zvolte Peugeot nebo Škoda) ")

if uzivatel_pozadovana_znacka == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
    print(auto1.pujc_auto())
    print(auto1.vrat_auto(2000, 11))
elif uzivatel_pozadovana_znacka == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
    print(auto2.pujc_auto())
    print(auto2.vrat_auto(111, 2))
else:
    print("Zadal/a jste neplatnou značku vozidla.")