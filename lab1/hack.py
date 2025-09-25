from caesar import decrypt

frequency_letter = {
    'e': 12.70, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97,
    'n': 6.75, 's': 6.33, 'h': 6.09, 'r': 5.99, 'd': 4.25,
    'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36,
    'f': 2.23, 'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.49,
    'v': 0.98, 'k': 0.77, 'x': 0.15, 'j': 0.15, 'q': 0.10, 'z': 0.07
}

def hack(ciphertext: str) -> tuple[str, int]:
    best_match = -1.0
    best_shift = 0
    best_text = ""

    shift = 0
    while shift < 26:
        decrypted_text = decrypt(ciphertext, shift)

        total = 0
        counts = {}
        i = 0
        while i < len(decrypted_text):
            ch = decrypted_text[i].lower()
            if 'a' <= ch <= 'z':
                total += 1
                if ch in counts:
                    counts[ch] += 1
                else:
                    counts[ch] = 1
            i += 1

       
        freq_dec = {}
        for letter in frequency_letter:
            if total > 0 and letter in counts:
                freq_dec[letter] = counts[letter] / total * 100
            else:
                freq_dec[letter] = 0.0

       
        match_quality = 0.0
        for letter in frequency_letter:
            a = freq_dec[letter]
            b = frequency_letter[letter]
            if a < b:
                match_quality += a
            else:
                match_quality += b

        if match_quality > best_match:
            best_match = match_quality
            best_shift = shift
            best_text = decrypted_text

        shift += 1

    return best_text, best_shift
