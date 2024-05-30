# Hirsipuu-peli

### Kuvaus

Ohjelma on Python kielellä ohjelmoitu hirsipuupeli. Teimme ohjelman kahden opiskelijan ryhmässä johon kuului Oskar Hänninen ja Eemeli Lehesalo. Pelaajan tulee arvata salainen sana kirjain kerrallaan. Pelaajalla on rajallinen määrä yrityksiä arvata kaikki oikein ennen kuin "hirttopuuhun" piirretty kuva valmistuu. Pelimoottoriin on annettu lista hedelmien nimiä Suomen kielellä joita pelaaja yrittää arvata.



### Toiminnot

**Sanan arvaaminen:** Pelaaja arvaa kirjaimia saadakseen selville salaisen sanan.

**Yritysten laskeminen:** Pelaajalla on tietty määrä yrityksiä, jotka vähenevät jokaisesta väärästä arvauksesta.

**Sanan näyttäminen:** Näyttää oikein arvatut kirjaimet ja korvaa arvaamattomat kirjaimet alaviivoilla.

**Pelin lopettaminen:** Ilmoittaa voitosta, jos sana arvataan oikein, tai häviöstä, jos yritykset loppuvat.

**Sanan valinta:** Ohjelma valitsee satunnaisen sanan valmiista sanalistasta.

**Käyttöliittymä:** Tekstipohjainen käyttöliittymä, joka näyttää pelaajalle tarvittavat tiedot ja vastaanottaa syötteet.

**Pelin logiikka:** Ohjelma seuraa pelaajan arvauksia, päivittää näytettävän sanan ja tarkistaa pelin voitto- tai häviötilanteen.



### Toteutus

**Koodikieli:** Python

**Yhteistyöalusta:** [Replit](https://replit.com/)

**Video:** [YouTube video](https://youtu.be/M3QHygdoEm4)

**Työnkulku:** Aluksi ladattiin koodiin 'random'-moduuli Python standardikirjastosta jonka avulla pystytään generoimaan satunnaisesti asioita. Sen jälkeen kirjoitettiin tervetuloa-teksti ja listattiin vähän pelin säännöistä. Kirjoitettiin 'sanapankki' muuttujaan lista hedelmiä suomenkielellä.

Tarvitsimme oikein ja väärin vastauksille ratkaisut siten että väärästä vastauksesta hirsipuun kuva kasvaisi ja oikeinvastauksesta tulisi esiin kirjainvinkki Hirsipuu sanalle.
Kirjoitimme funktion joka määrittää tulostettavan tekstin (kuvan) kun vastaus on väärin ja laskurin kuinka monta kertaa on vastattu oikein tai väärin. Tarvitsimme myös funktion joka tarkistaa käytetyt kirjaimet ja oliko ne oikein.

Tarvitsimme funktion, joka laskee ja tarkastaa oikein vastatut merkit ja näyttää ne pelaajalle. Käytimme myös funktiota joka näyttää pelaajalle jos hän läpäisi pelin, tai jos pelaaja ei päässyt peliä läpi.

![Vuokaavio](/Hirsipuupelin%20vuokaavio.jpg)