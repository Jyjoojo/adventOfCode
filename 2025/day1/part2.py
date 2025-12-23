def main():
    import os
    # Lecture des rapports depuis le fichier input.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")
    
    with open(input_file, "r") as f:
        data = [(line[0], int(line[1:])) for line in f if line.strip()]

    total_zeros = 0
    cadran_value = 50

    for direction, number in data:
        if direction == 'R':
            # On compte combien de multiples de 100 on atteint/dépasse
            # Exemple : pos 95 + R10 -> (95+10)//100 = 1 passage à zéro
            total_zeros += (cadran_value + number) // 100
            
            # Nouvelle position
            cadran_value = (cadran_value + number) % 100
        else:
            # Cas spécial : si on est déjà sur 0, le premier clic vers 
            # la gauche nous met à 99. On ne touchera le 0 qu'après 100 clics.
            temp_pos = cadran_value if cadran_value > 0 else 100
            
            if number >= temp_pos:
                # Le premier passage est à 'temp_pos' clics.
                # Les suivants sont tous les 100 clics.
                total_zeros += 1 + (number - temp_pos) // 100
            
            # Nouvelle position (Python gère très bien le modulo négatif)
            cadran_value = (cadran_value - number) % 100

    print(f"Le nouveau mot de passe est : {total_zeros}")

if __name__ == "__main__":
    main()