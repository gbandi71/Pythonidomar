#! /usr/bin/env python3

'''
F0003a: Írj programot, amely külön-külön megkérdi a vezeték- 
és a keresztneved, majd kiírja őket egy mondatban, pl: A 
te neved Kovács Boldizsár. (A pontot se felejtsd el!)

vnev változóba kérni a vezetéknevet
knev változóba kérni a keresztnevet
kiíratás
'''
vnev = input('Kérem a vezetékneved: ')
knev = input('Kérem a keresztneved: ')
print('A te neved: ', vnev,' ', knev,'.', sep='')
