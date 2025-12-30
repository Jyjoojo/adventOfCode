def is_periodic(n):
    """Vérifie si un nombre est composé d'une séquence répétée."""
    s = str(n)
    # L'astuce : on cherche s dans (s+s) en ignorant les index extrêmes
    return (s + s).find(s, 1, -1) != -1

def main():
    import os
    # Lecture des rapports depuis le fichier input.txt
    script_dir = os.path.dirname(os.path.abspath(__file__))
    input_file = os.path.join(script_dir, "input.txt")
    
    # data = []
    with open(input_file, "r") as f:
        data = [
            (int(el.split("-")[0]), int(el.split("-")[1])) 
            for line in f 
            for el in line.strip().split(",") 
            if "-" in el
        ]
    #     for line in f:
    #         l = line.split(",")
    # for el in l:
    #     liste = el.split("-")
    #     data.append((int(liste[0]), int(liste[-1])))
    # print(data)
    cpt = 0
    for el in data:
        for i in range(el[0],el[1]+1):
            if is_periodic(i)== True:
                cpt+=i
    print(f"La somme des ID invalides est: {cpt}")


main()