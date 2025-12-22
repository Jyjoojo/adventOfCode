def main():
    import os
    # Lecture des rapports depuis le fichier input.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")
    with open(input_file, "r") as f:
        data = [(line[0], int(line[1:])) for line in f if line.strip()]

    # Compteurs
    nb_of_zero = 0
    cadran_value = 50

    for row in data:
        number = row[1]
        direction = row[0]
        if direction == 'L':
            cadran_value = (cadran_value - number) % 100
        else:
            cadran_value = (cadran_value + number) % 100
        if cadran_value == 0:
            nb_of_zero += 1
    print("Le nombre de fois le cadran atteint 0 est :", nb_of_zero)
if __name__ == "__main__":
    main()