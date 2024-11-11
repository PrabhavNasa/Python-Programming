def count_characters(s):
    vowels = "aeiouAEIOU"
    v = c = b = 0
    for char in s:
        if char in vowels:
            v += 1
        elif char.isalpha():
            c += 1
        elif char == ' ':
            b += 1
    return v, c, b

s = "\nThis program is written by Prabhav. \nERPID: 0221BCA011\n"
print(s)
v, c, b = count_characters(s)
print("Vowels:", v, "Consonants:", c, "Blanks:", b)


