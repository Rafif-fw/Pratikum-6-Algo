# -*- coding: utf-8 -*-
"""
Created on Thu Oct 27 19:54:58 2022

@author: Rafif Fernanda
"""

def bulan():
 print("Ini adalah program yang bisa menentukan hari dalam bulan")
 while True:
  print("Tekan 0 untuk menghentikan program")
  x = int(input('Sekarang bulan ke berapa(1-12): '))
  if(x == 1 or x == 3 or x == 5 or x == 7 or x == 8 or x == 10 or x == 12):
   print(' Jumlah harinya adalah 31\n')
  elif(x == 2):
   print(' Jumlah harinya adalah 28\n')
  elif x == 0 :
   print("Terima kasih sudah menggunakan program saya, sampai berjumpa lagi.\n")
   break
  else:
   print(' Jumlah harinya adalah 30\n')
 
B = bulan()
print(B)