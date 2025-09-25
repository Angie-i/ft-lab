from caesar import encrypt, decrypt
from collections import Counter
frequency_letter = {'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
        'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
        'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
        'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.49,
        'v': 0.98, 'k': 0.77, 'x': 0.15, 'j': 0.15, 'q': 0.10, 'z': 0.07}
def hack(ciphertext: str) -> tuple[str, int]:
        best_match=0
        best_shift=0
        best_text=''
        l=len(ciphertext)
        for x in range(26):
                decrypted_text = decrypt(ciphertext, x)
                frequency_decypt={}
                for x, y in Counter(decrypted_text).items():
                        if x.upper() in frequency_letter:
                                frequency_decypt[x.upper()]= y/l*100
                match_quality = sum(min(frequency_decypt.get(letter, 0), frequency_letter[letter])
                                  for letter in frequency_letter)
                if best_match< match_quality:
                        best_match=match_quality
                        best_shift=x
                        best_text=decrypted_text
        return best_text,best_shift
