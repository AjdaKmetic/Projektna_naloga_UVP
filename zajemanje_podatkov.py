import re
import requests
import os

# link = 'https://fbref.com/en/comps/9/2023-2024/stats/2023-2024-Premier-League-Stats'
# igralci_mapa = 'podatki'
# igralci_html = 'igralci.html'

def url_v_niz(url):
    odgovor = requests.get(url)
    if odgovor.status_code == 200:
        vsebina_html = odgovor.text
        return vsebina_html
    else:
        print('Prišlo je do napake pri pridobivanju strani.')

def shrani_niz_v_datoteko(vsebina, mapa, datoteka):
    os.makedirs(mapa, exist_ok=True)
    pot = os.path.join(mapa, datoteka)
    with open(pot, 'w', encoding='utf-8') as dat:
        print(vsebina, file=dat)
    return None

def shrani_stran(url, mapa, datoteka):
    vsebina_html = url_v_niz(url)
    shrani_niz_v_datoteko(vsebina_html, mapa, datoteka)

# shrani_stran(link, igralci_mapa, igralci_html)

# izluščimo podatke:

def vsebina_datoteke_v_niz(mapa, datoteka):
    cela_pot = os.path.join(mapa, datoteka)
    with open(cela_pot, 'r', encoding='utf-8') as dat:
        return dat.read()

def izlusci_igralce(niz):
    vzorec = r'<tr ><th scope="row" class="right " data-stat="ranker" >.+?</a></td></tr>'
    return re.findall(vzorec, niz, flags=re.DOTALL)

# seznam_igralcev = izlusci_igralce(vsebina_html)

# for igralec in seznam_igralcev:
#     print(igralec)

def izlusci_podatke(niz):
    vzorec_ime = r'<a href="/en/players/.*?">(?P<ime>.*?)</a>'
    vzorec_narodnost = r'<a href="/en/country/.*?</span> (?P<narodnost>[A-Z]{3})</span></a>'
    vzorec_polozaj = r'<td class="center " data-stat="position" csk="\d\.\d" >(?P<polozaj>.*?)</td>'
    vzorec_ekipa = r'<a href="/en/squads/.*?">(?P<ekipa>.*?)</a>'
    vzorec_starost = r'<td class="center " data-stat="age" >(?P<starost>\d{2})</td>'
    vzorec_odigrane_tekme = r'<td class="right group_start" data-stat="games" >(?P<st_odigranih_tekem>\d{1,2})</td>'
    vzorec_minute = r'<td class="right " data-stat="minutes" csk="\d+" >(?P<minute>(\d|,)+)</td>'
    vzorec_goli = r'<td class=".*?" data-stat="goals" >(?P<st_golov>\d+)</td>'
    vzorec_asistence = r'<td class=".*?" data-stat="assists" >(?P<st_asistenc>\d+)</td>'
    vzorec_rumeni_kartoni = r'<td class=".*?" data-stat="cards_yellow" >(?P<rumeni_kartoni>\d+)</td>'
    vzorec_rdeci_kartoni = r'<td class=".*?" data-stat="cards_red" >(?P<rdeci_kartoni>\d+)</td>'

    ime = re.search(vzorec_ime, niz).group('ime')
    narodnost = re.search(vzorec_narodnost, niz).group('narodnost')
    polozaj = re.search(vzorec_polozaj, niz).group('polozaj')
    ekipa = re.search(vzorec_ekipa, niz).group('ekipa')
    starost = re.search(vzorec_starost, niz).group('starost')
    st_odigranih_tekem = re.search(vzorec_odigrane_tekme, niz).group('st_odigranih_tekem')
    minute = re.search(vzorec_minute, niz).group('minute')
    st_golov = re.search(vzorec_goli, niz).group('st_golov')
    st_asistenc = re.search(vzorec_asistence, niz).group('st_asistenc')
    rumeni_kartoni = re.search(vzorec_rumeni_kartoni, niz).group('rumeni_kartoni')
    rdeci_kartoni = re.search(vzorec_rdeci_kartoni, niz).group('rdeci_kartoni')

    return {
        'Ime': ime,
        'Narodnost': narodnost,
        'Položaj': polozaj.replace(',', ', '),
        'Ekipa': ekipa,
        'Starost': int(starost),
        'Odigrane tekme': int(st_odigranih_tekem),
        'Minute': int(minute.replace(',', '')),
        'Goli': int(st_golov),
        'Asistence': int(st_asistenc),
        'Rumeni kartoni': int(rumeni_kartoni),
        'Rdeči kartoni': int(rdeci_kartoni)
    }

# vsebina_html = url_v_niz(link)

# for igralec in izlusci_igralce(vsebina_html):
#   print(izlusci_podatke(igralec))

def igralci_iz_datoteke(mapa, datoteka):
    vsebina = vsebina_datoteke_v_niz(mapa, datoteka)
    igralci = izlusci_igralce(vsebina)
    sez_slovarjev = []
    for igralec in igralci:
        sez_slovarjev.append(izlusci_podatke(igralec))
    return sez_slovarjev

# print(igralci_iz_datoteke(igralci_mapa, igralci_html))