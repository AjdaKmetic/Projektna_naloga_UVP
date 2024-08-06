from zajemanje_podatkov import *
from shranjevanje_podatkov import *

def main():
    link = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats'
    igralci_mapa = 'podatki'
    igralci_html = 'igralci.html'
    igralci_csv = 'igralci.csv'

    # Najprej v lokalno datoteko shranimo glavno stran
    # pot1 = os.path.join(igralci_mapa, igralci_html)
    # if redownload or not os.path.exists(pot1):
    shrani_stran(link, igralci_mapa, igralci_html)

    # Podatke preberemo v lepšo obliko (seznam slovarjev)
    seznam_igralcev = igralci_iz_datoteke(igralci_mapa, igralci_html)

    # Podatke shranimo v csv datoteko
    # pot2 = os.path.join(igralci_mapa, igralci_csv)
    # if reparse or not os.path.exists(pot2):
    zapisi_igralce_v_csv(seznam_igralcev, igralci_mapa, igralci_csv)

if __name__ == '__main__':
    main()