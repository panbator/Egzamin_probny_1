def shorten(string):
    # Rozdzielenie napisu na słowa
    words = string.split()

    # Utworzenie skrótu z pierwszych liter słów
    acronym = ""
    for word in words:
        acronym += word[0].upper()

    return acronym


if __name__ == '__main__':

    shortened = shorten("Don't repeat yourself")

    print(shortened)


    shortened = shorten("Rage Against The Machine")

    print(shortened)