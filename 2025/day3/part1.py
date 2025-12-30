import os

def solve():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")
    
    total_output_joltage = 0

    if not os.path.exists(input_file):
        print("Fichier input.txt introuvable")
        return

    with open(input_file, "r") as f:
        for line in f:
            bank = line.strip()
            if not bank:
                continue
            
            # On transforme la ligne en liste de chiffres
            digits = [int(d) for d in bank]
            max_bank_joltage = 0
            
            # On teste toutes les combinaisons possibles (i avant j)
            for i in range(len(digits) - 1):
                for j in range(i + 1, len(digits)):
                    current_joltage = digits[i] * 10 + digits[j]
                    if current_joltage > max_bank_joltage:
                        max_bank_joltage = current_joltage
            
            total_output_joltage += max_bank_joltage

    print(f"The total output joltage is: {total_output_joltage}")

if __name__ == "__main__":
    solve()