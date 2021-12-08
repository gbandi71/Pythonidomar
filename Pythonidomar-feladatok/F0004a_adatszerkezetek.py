#! /usr/bin/env python3
'''
név = input('Hogy híjják kendet? ')
kor = input('És hány éves kend? ') # itt még stringet kapunk
kor = int(kor) # átalakítjuk egész számmá, azaz int-té
születési_év = 2016 - kor
print(név, ', kend ', születési_év, '-ban született.', sep='')
F0004a: Bővítsük a fenti programot úgy, hogy jövőálló legyen: kérdezze meg a felhasználót,
hogy melyik év van, és ezt vegye figyelembe, azaz ne mindig 2016-tal
számoljon!

vnev bekér
knev bekér
kor bekér
akt_ev bekér

kor (int) egésszé alakít
akt_ev (int) egésszé alakít
akt_ev-ből kivon kor megkap sz_ev
ki: ('\n', vnev,' ', knev,'. ', sz_ev,'-ban született! ', sep='')
'''
vnev = input('Kérem a vezetékneved: ')
knev = input('Kérem a keresztneved: ')
kor = input('Hány éves vagy? ')
akt_ev = input('Milyen évet írunk most? ')

kor = int(kor)
akt_ev = int(akt_ev)

sz_ev = akt_ev - kor

print('\n', vnev,' ', knev,'. ', sz_ev,'-ban született! ', sep='')
