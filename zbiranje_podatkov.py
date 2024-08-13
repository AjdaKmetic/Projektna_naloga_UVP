from zajemanje_podatkov import *
from shranjevanje_podatkov import *

def main():
    link = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats'
    igralci_mapa = 'podatki'
    igralci_html = 'igralci.html'
    igralci_csv = 'igralci.csv'

    shrani_stran(link, igralci_mapa, igralci_html)

    seznam_igralcev = igralci_iz_datoteke(igralci_mapa, igralci_html)

    zapisi_igralce_v_csv(seznam_igralcev, igralci_mapa, igralci_csv)

if __name__ == '__main__':
    main()