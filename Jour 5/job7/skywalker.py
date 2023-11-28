def arrondir_notes(notes):
    notes_arrondies = []

    for note in notes:
        if note < 40:
            notes_arrondies.append(note)
        else:
            difference = 5 - (note % 5)
            if difference < 3:
                note_arrondie = note + difference
                notes_arrondies.append(note_arrondie)
            else:
                notes_arrondies.append(note)

    return notes_arrondies

notes_etudiants = [37, 58, 82, 91, 45]
notes_arrondies = arrondir_notes(notes_etudiants)
print("Notes initiales :", notes_etudiants)
print("Notes arrondies :", notes_arrondies)
