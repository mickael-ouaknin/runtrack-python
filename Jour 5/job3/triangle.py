def draw_triangle(height):
    for i in range(height):
        espaces = height - i - 1

        print(' ' * espaces + '/' + ' ' * (2 * i) + '\\')

hauteur = int(input("Entrez la hauteur du triangle : "))

draw_triangle(hauteur)