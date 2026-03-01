VOWELS = 'aeiou'

def check_for_vowels(text):
    for char in text:
        if char in VOWELS:
            return True
    return False

def find_first_vowel(text):
    for index, char in enumerate(text):
        if char in VOWELS:
            return index
    return False

def translate(text):
    res = []
    for word in text.split(' '):
        if check_for_vowels(word[0]) or word[0:2] in ['xr', 'yt']:
            res.append(f'{word}ay')
        else:
            if (word.find('qu') < 0 and word.find('y') <= 0) or (check_for_vowels(word[0:word.find('qu')]) and check_for_vowels(word[0:word.find('y')])):
                # answer is not qu or y
                # if word in ['queen', 'quick', 'square']:return not check_for_vowels(word[0:word.find('qu')])
                res.append(f'{word[find_first_vowel(word):]}{word[0:find_first_vowel(word)]}ay')
            else:
                if word.find('qu') >= 0 and (word.find('qu') < word.find('y') or word.find('y') == -1):
                    # do the qu one
                    # if word in ['queen', 'quick', 'square']:return 2
                    # find_first_vowel should return index of the u in 'qu'
                    res.append(f'{word[find_first_vowel(word) + 1:]}{word[0:find_first_vowel(word) + 1]}ay')
                else:
                    # do the y one
                    res.append(f'{word[word.find('y'):]}{word[0:word.find('y')]}ay')

    return ' '.join(res)
