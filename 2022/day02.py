with open("./data/day02.txt") as f:

    scoring = {"W": 6, "D": 3, "L": 0, "X": 1, "Y": 2, "Z": 3}
    total_score = 0

    for line in f.readlines():

        opp, you = line.split()

        total_score += scoring[you]

        if opp == "A":
            if you == "X":
                total_score += scoring["D"]
            if you == "Y":
                total_score += scoring["W"]
            if you == "Z":
                total_score += scoring["L"]

        if opp == "B":
            if you == "X":
                total_score += scoring["L"]
            if you == "Y":
                total_score += scoring["D"]
            if you == "Z":
                total_score += scoring["W"]

        if opp == "C":
            if you == "X":
                total_score += scoring["W"]
            if you == "Y":
                total_score += scoring["L"]
            if you == "Z":
                total_score += scoring["D"]


print(total_score)
