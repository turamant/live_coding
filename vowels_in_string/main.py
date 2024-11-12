# Напиши функцию, которая принимает строку и возвращает количество гласных букв в этой строке.
#  Гласные буквы: 'a', 'e', 'i', 'o', 'u' (в любом регистре).

# Когда будешь готов, просто напиши свое решение!

letter = ['a', 'e', 'i', 'o', 'u']

def count_vowels_in_string(word: str)-> int:
    count = 0
    word = word.lower()
    for i in word:
        if i in letter:
            count +=1 
    return count


if __name__ == '__main__':
    print(count_vowels_in_string("make"))
    print(count_vowels_in_string("congratilation"))
    print(count_vowels_in_string("The best"))
    print(count_vowels_in_string("The OIEbest"))