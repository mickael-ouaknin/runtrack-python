def fruit_saison(type, saison):
    if type == "fruits" and saison == "hiver":
        return ["orange", "mandarine", "kiwi"]
    elif type == "fruits" and saison == "été":
        return ["poire", "fraise", "cassis"]
    elif type == "légumes" and saison == "hiver":
        return ["carotte", "topinambour", "endive"]
    elif type == "légumes" and saison == "été":
        return ["artichaut", "aubergine", "navet"]
    else:
        return []


type_input = input("Type (fruits/légumes): ")
saison_input = input("Saison (hiver/été): ")

result = fruit_saison(type_input, saison_input)
print(result)