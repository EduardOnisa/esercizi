#Dato un intero x, restituisce True se x è palindromo, e False altrimenti

def is_palindrome(x: 135) -> bool:
    s: str = str(x)
    s1= "".join(reversed(s))
    return s == s1
out = is_palindrome(135)
print(out)


#Data una stringa s che contiene parole e spazi, restituire la lunghezza dell'ultima parola in s

def length_of_last_word(s: str) -> int:
    l: list[str] = s.split()
    return len(1[-1])




#Dato un intero col_number, restituire il suo corrispondente titolo di colonna come ad esempio compare su un foglio Excel

    def convert_to_title(col_number: int) -> str: 
        result: str = ""
        while col_number > 0:
            resto: int = (col_number- 1) % 26 #resto
            result = chr(resto + ord ('A')) + result
            col_number = (col_number - 1) // 26
        return result 
    

    