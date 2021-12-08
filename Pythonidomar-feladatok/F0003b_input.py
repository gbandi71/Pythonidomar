#! /usr/bin/env python3

'''
F0003b: Bővítsd az előző programot úgy, hogy a kiírás 
előtt kérdezze meg a születési évedet és a 
csillagjegyedet, és az előző feladatban megadott mondat 
után ezt is közölje veled.

vnev változóba kérni a vezetéknevet
knev változóba kérni a keresztnevet
szev változóba kérni a születési évet
csjegy változóba kérni a csillagjegyet
ki: ('\nA te neved: ', vnev,' ', knev,'.\nA születési éved: ', szev,'.\nA csillag jegyed: ', csjegy, sep='')
'''
vnev = input('Kérem a vezetékneved: ')
knev = input('Kérem a keresztneved: ')
szev = input('Kérem a születési évedet: ')
csjegy = input('Kérem a csillagjegyedet: ')
print('\nA te neved: ', vnev,' ', knev,'.\nA születési éved: ', szev,'.\nA csillag jegyed: ', csjegy, sep='')
