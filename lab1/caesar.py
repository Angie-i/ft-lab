ASCII_MAX = 126                        
ASCII_MIN = 32
ALF = ASCII_MAX - ASCII_MIN + 1
def encrypt(plaintext: str, shift: int) -> str: 
    '''
    Шифровка текста с помощью шифра Цезаря.
    :param plaintext: исходный текст
    :param shift: целое число для сдвига 
    :return: зашифровеный текст
    '''
    result = ''
    if shift !=0:
        for i in plaintext :                  
            num = ord(i) - ASCII_MIN           #перевод в систему 0-95  
            index = (num + shift) % ALF        #отброс "полных" кругов по 95 символов  
            new_num = ASCII_MIN + index        #возвращение к ASCII  
            result += (chr(new_num))            
        return result 
    else:
        return plaintext

def decrypt(ciphertext: str, shift: int) -> str: 
    '''
    Дешифрует текст, зашифрованный шифром Цезаря, используя функцию encrypt с отрицательным сдвигом. 
    :param ciphertext: зашифрованный текст 
    :param shift: целое число сдвига использованное для шифровки 
    :return: расшифрованный текст 
    '''
    return encrypt(ciphertext,-shift)
    
