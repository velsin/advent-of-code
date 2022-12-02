with open("./data/day02.txt") as f:

    scoring = {"W": 6, "D": 3, "L": 0, "X": 0, "Y": 3, "Z": 6, "A": 1, "B": 2, "C": 3}

    total_score = 0

    for line in f.readlines():

        opp, you = line.split()

        total_score += scoring[you]

        if opp == "A":
            if you == "X":
                total_score += scoring["C"]
            if you == "Y":
                total_score += scoring["A"]
            if you == "Z":
                total_score += scoring["B"]

        if opp == "B":
            if you == "X":
                total_score += scoring["A"]
            if you == "Y":
                total_score += scoring["B"]
            if you == "Z":
                total_score += scoring["C"]

        if opp == "C":
            if you == "X":
                total_score += scoring["B"]
            if you == "Y":
                total_score += scoring["C"]
            if you == "Z":
                total_score += scoring["A"]


print(total_score)
