def isValid(n):
    s = str(n)
    size = len(s)
    
    if size % 2 != 0:
        return True
    
    middle = size // 2 
    left_part = s[:middle]
    right_part = s[middle:]

    if left_part == right_part:
        return False
    else:
        return True

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
            if isValid(i)== False:
                cpt+=i
    print(f"La somme des ID invalides est: {cpt}")


main()