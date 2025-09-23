ASCII_MAX = 126                        
ASCII_MIN = 32
ALF = ASCII_MAX - ASCII_MIN + 1
def encrypt(plaintext: str, keyword: str) -> str:
    shifts=[]
    result=''
    counter=0
    for i in keyword:
        letter=i.upper()
        if 'A' <= letter <= 'Z':
            shifts.append(ord(letter) - ord('A'))
    if len(shifts)==0:
        return plaintext
    for r in plaintext:
        s=shifts[counter % len(shifts)]
        index=ord(r) - ASCII_MIN
        new_index=(index + s)% ALF
        new_code=ASCII_MIN + new_index
        new_char=chr(new_code)
        result += new_char
        counter+=1
    return result

def decrypt(chipherntext: str, keyword: str) -> str:
    shifts=[]
    result=''
    counter=0
    for i in keyword:
        letter=i.upper()
        if 'A' <= letter <= 'Z':
            shifts.append(ord(letter) - ord('A'))
    if len(shifts)==0:
        return chipherntext
    for r in chipherntext:
        s=shifts[counter % len(shifts)]
        index=ord(r) - ASCII_MIN
        new_index=(index - s)% ALF
        new_code=ASCII_MIN + new_index
        new_char=chr(new_code)
        result += new_char
        counter+=1
    return result
  
    
  
