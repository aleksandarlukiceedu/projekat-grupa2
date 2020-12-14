from korisnici.korisnik import prijava
from knjige.knjiga import prikazi_knjige, pretrazi_knjige


def meni_administrator(ulogovani_korisnik):
    while True:
        print("\n1. Prikaz knjiga")
        print("2. Pretraga knjiga")
        print("3. Prikaz akcija")
        print("4. Pretraga akcija")
        print("10. Kraj")

        stavka = int(input("Izaberite stavku: "))

        if stavka == 1:
            prikazi_knjige()
        elif stavka == 2:
            pretrazi_knjige()
        elif stavka == 10:
            return
        else:
            print("Pogresan izbor!")


def main():
    ulogovani_korisnik = prijava()

    if ulogovani_korisnik is not None:
        if ulogovani_korisnik['tip_korisnika'] == 'Administrator':
            meni_administrator(ulogovani_korisnik)
        elif ulogovani_korisnik['tip_korisnika'] == 'Menzdzer':
            pass
        elif ulogovani_korisnik['tip_korisnika'] == 'Prodavac':
            pass
        else:
            print("Greska! Korisnik ima nepostojecu ulogu!")


main()
