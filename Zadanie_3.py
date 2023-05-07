def check_palindrome(text):
    # Usunięcie spacji i zamiana na małe litery
    text = text.replace(' ', '').lower()

    # Sprawdzenie, czy zdanie jest palindromem
    if text == text[::-1]:
        return True
    else:
        return False


text = "Kobyła ma mały bok"
print(check_palindrome(text))  # True

text = "Ala ma kota"
print(check_palindrome(text))  # False
