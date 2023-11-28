def chiffrement_cesar(message, decalage):
    resultat = ""
    for char in message:
        if char.isalpha():
            minuscule = char.islower()
            char = char.lower()
            code_ascii = ord(char)
            code_ascii_decale = (code_ascii - ord('a') + decalage) % 26 + ord('a')
            if minuscule:
                resultat += chr(code_ascii_decale)
            else:
                resultat += chr(code_ascii_decale).upper()
        else:
            resultat += char
    return resultat

message = int(input("Entrez la hauteur du triangle : "))
message = "Bonjour, Jules Cesar"
decalage = 3
message_chiffre = chiffrement_cesar(message, decalage)
print(f"Message initial : {message}")
print(f"Message chiffré : {message_chiffre}")