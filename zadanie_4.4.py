#import sys
import logging
#logging.basicConfig(level=logging.debug)

choose_operation = input("Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie / 2 Odejmowanie / 3 Mnożenie / 4 Dzielenie:")

def add(x,y):
    return x + y
    

if choose_operation == '1':
    number1 = logging.info (int(input("Podaj składnik 1:")))
    number2 = logging.info (int(input("Podaj składnik 2:")))
    #logging.info(f"Dodaję {number1} i {number2}")
    result = add(number1, number2)
    print (result)

else:
    exit
    



