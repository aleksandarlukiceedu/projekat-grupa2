from knjige.knjigaIO import ucitaj_knjige


def sortiraj_knjige(kljuc):
    knjige = ucitaj_knjige()

    n = len(knjige)

    for j in range(n):
        for i in range(n-j-1):
            if knjige[i][kljuc] > knjige[i+1][kljuc]:
                temp = knjige[i]
                knjige[i] = knjige[i+1]
                knjige[i+1] = temp

    return knjige


def prikazi_knjige():
    print("\n--------Prikaz knjiga--------")
    print("1. Sortiraj po naslovu")
    print("2. Soritraj po kategoriji")
    print("3. Sortiraj po autoru")
    print("-----------------------------")
    stavka = int(input("Izaberite stavku: "))
    knjige = []

    if stavka == 1:
        knjige = sortiraj_knjige("naslov")
    elif stavka == 2:
        knjige = sortiraj_knjige("kategorija")
    elif stavka == 3:
        knjige = sortiraj_knjige("autor")

    for knjiga in knjige:
        print(knjiga)


def pretraga_po_jednakosti(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if knjiga[kljuc] == vrednost:
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretraga_string(kljuc, vrednost):
    knjige = ucitaj_knjige()
    filtrirane_knjige = []

    for knjiga in knjige:
        if vrednost.lower() in knjiga[kljuc].lower():
            filtrirane_knjige.append(knjiga)

    return filtrirane_knjige

def pretrazi_knjige():
    print("\n--------Pretraga knjiga--------")
    print("1. Pretraga po sifri")
    print("2. Pretraga po naslovu")
    print("3. Pretraga po autoru")
    print("4. Pretraga po kategoriji")
    print("-----------------------------")

    stavka = int(input("Izaberite stavku: "))
    knjige = []

    if stavka == 1:
        sifra = int(input("unesite sifru: "))
        knjige = pretraga_po_jednakosti('sifra', sifra)
    elif stavka == 2:
        naslov = input("unesite naslov: ")
        knjige = pretraga_string('naslov', naslov)
    elif stavka == 3:
        autor = input("unesite autora: ")
        knjige = pretraga_string("autor", autor)

    for knjiga in knjige:
        print(knjiga)
