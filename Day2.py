
with open("Day2txt") as f:
    games = f.readlines()
    print(games)



def Day2A(games):
    total = 0
    for game in games:
        good = True
        idx, line = game.split(":")
        for hand in line.split(";"):
            colour_count = [0,0,0]
            for balls in hand.split(","):
                n, colour = balls.split()
                colour_count[{'red':0,"blue":1,"green":2}.get(colour, 0)] += int(n)
                if (colour_count[0] > 12) or (colour_count[1] > 13) or (colour_count[2] > 14):
                    good = False
        if good:
            total += int(idx.split(' ')[1])
    print(total)

Day2A(games)