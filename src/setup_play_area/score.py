def update_score(nscore):
    score = max_score()
    with open("scores.txt", "w") as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))


def max_score():
    if not open("scores.txt", "a+"):
        open("scores.txt", "x")

    with open("scores.txt", "r") as f:
        lines = f.readlines()
        if lines:
            score = int(lines[0].strip())
        else:
            score = 0

    return score
