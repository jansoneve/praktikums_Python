""" 
Uzrakstiet programmu, kas ielasa skaitli (kā float) -
riņķa līnijas rādiusu un izvada uz ekrāna (print) 
riņķa līnijas garumu un laukumu, atbilstoši noformējot atbildi.
Pārbaudiet programmas darbību ar dažādiem ievaddatiem.
"""
import math

radiuss=float(input("Ievadi riņķa līnijas rādiusu cm: "))

garums=2*math.pi*radiuss
laukums=math.pi*pow(radiuss,2)

print("Riņķa līnijas garums ir ",garums,"cm. Riņķa līnijas laukums ir ",laukums,"cm.")
