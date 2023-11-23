num1 = float(input("nombre : "))
operator = input("choisit un operateur (+, -, *, /, %) : ")
num2 = float(input("un deuxieme : "))

def calcule(num1, operator, num2):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 != 0:  
            return num1 / num2
        else:
            raise ValueError("Division par zéro.")
    elif operator == "%":
        return num1 % num2
    else:
        raise ValueError("Opérateur inconnu.")

result = calcule(num1, operator, num2)
print("Résultat :", result)   