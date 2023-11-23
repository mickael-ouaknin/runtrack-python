print("Alphabet en majuscules à l'envers:")
for i in range(ord('Z'), ord('A')-1, -1):
    print(chr(i), end=' ')
print()

print("\nAlphabet en minuscules à l'envers:")
for i in range(ord('z'), ord('a')-1, -1):
    print(chr(i), end=' ')
print()