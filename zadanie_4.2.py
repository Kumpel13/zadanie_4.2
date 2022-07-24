
def is_it_palindrome(palindrome):
    """ 
    Funkcja sprawdza czy słowo napisane od końca, 
    jest takie samo jak napisane normalnie,
    Jeśli tak to printuje "True", jeśli nie "False" 
    """
    if palindrome == palindrome[::-1]:
        return True
    else:
        return False    

print (is_it_palindrome("kajak"))
print (is_it_palindrome("Kuter"))