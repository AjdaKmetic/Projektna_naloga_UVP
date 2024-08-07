from zajemanje_podatkov import *
import os
import csv

def shrani_csv(imena_stolpcev, vrstice, mapa, datoteka):
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'w', encoding='utf-8') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=imena_stolpcev)
        writer.writeheader()
        writer.writerows(vrstice)
    return

def zapisi_igralce_v_csv(igralci, mapa, datoteka):
    assert igralci and (all(i.keys() == igralci[0].keys() for i in igralci))
    imena_stolpcev = igralci[0].keys()
    shrani_csv(imena_stolpcev, igralci, mapa, datoteka)

# igralci_vrstice = igralci_iz_datoteke(igralci_mapa, igralci_html)
# igralci_csv = 'igralci.csv'

# zapisi_igralce_v_csv(igralci_vrstice, igralci_mapa, igralci_csv)