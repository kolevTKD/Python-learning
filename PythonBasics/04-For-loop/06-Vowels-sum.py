text = input()
vowels_sum = 0

for i in range (0, len(text)):
    char = text[i]
    if char == 'a':
        vowels_sum += 1
    elif char == 'e':
        vowels_sum += 2
    elif char == 'i':
        vowels_sum += 3
    elif char == 'o':
        vowels_sum += 4
    elif char == 'u':
        vowels_sum += 5

print(vowels_sum)